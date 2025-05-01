#!/usr/bin/env python3

import os
import json
import shutil
import requests
from pathlib import Path
from ghapi.all import GhApi
from rich import print
from .queryFilter import QueryFilter

class Version2Query:
  def __init__(self, temp_dir:str="tmp.dir", output_file:str="output.items.json"):
    self.temp_dir:Path = Path(temp_dir)
    self.output_file:str = output_file
    self.api:GhApi = GhApi()
    self._validate_token()
    self.filters:QueryFilter = QueryFilter()

  def _validate_token(self) -> None:
    """Validate Github token exists in the environment."""
    if not os.getenv("GITHUB_TOKEN"):
      raise ValueError("GITHUB_TOKEN environment variable is not set.")

  def set_filters(self, filters:dict) -> None:
    """Set filters for the query."""
    self.filters.set_filters_from_dict(filters)
    self.filters.print_filters()

  def get_github_token(self) -> str:
    return os.getenv("GITHUB_TOKEN")

  def get_github_orgs(self) -> list[str]:
    """Create a list of github orgs based on the authenticated user."""
    return [org["login"] for org in self.api.orgs.list_for_authenticated_user()]

  def get_all_projects(self, orgs:list[str]) -> list[dict]:
    """Get all projects for each org in orgs."""

    # Query projects for each org
    all_projects:list[dict] = []
    for org in orgs:
      print(f"[bold blue]Fetching projects for org: {org}[/bold blue]")

      # the graphql query needed to pull in all the data from gh api
      query:str = """
      query($login: String!) {
        organization(login: $login) {
          projectsV2(first: 100) {
            nodes {
              id
              number
              title
            }
          }
        }
      }
      """

      headers:dict = {"Authorization": f"Bearer {self.get_github_token()}"}
      response = requests.post(
        "https://api.github.com/graphql",
        json={"query": query, "variables": {"login": org}},
        headers=headers
      )

      result = response.json()
      projects:list[dict] = [
        {
          "org": org,
          "number": project["number"],
          "title": project["title"]
        }
        for project in result.get("data", {}).get("organization", {}).get("projectsV2", {}).get("nodes", [])
      ]

      all_projects.extend(projects)
    return all_projects

  def filter_projects_by_team(self, project_list:list[dict], teams:list[str]) -> list[dict]:
    """Filter the project list by team names."""

    filtered_projects:list[dict] = []
    for team in teams:
      matching_projects:list[dict] = [p for p in project_list if team.lower() in p["title"].lower()]

      filtered_projects.extend(matching_projects)
      print(f"[green]Found {len(matching_projects)} matching projects for team '{team}'[/green]")
    return filtered_projects

  def filter_items_by_user(self) -> None:
    """Filter items by user."""

    filtered_items:list[dict] = []

    # pull the data out of output.projects.json and write to that file again
    with open(self.output_file) as f:
      items = json.load(f)
      for item in items:
        for user in self.filters.include_users:
          if user in item.get("assignees", []):
            filtered_items.append(item)
            break # avoid appending the item multiple times if it matches multiple users.

    # move self.output_file to output.items.json.tmp
    tmp_file = self.output_file + ".tmp"

    # write the new output_file with the filter_items_by_user
    with open(self.output_file, "w") as f:
      json.dump(filtered_items, f, indent=2)

    # remove the tmp_file
    if Path(tmp_file).exists():
      os.remove(tmp_file)

  def fetch_project_items(self, projects:list[dict]) -> bool:
    """Fetch all items on each project."""

    rv:bool = True
    self.temp_dir.mkdir(exist_ok=True)
    for project in projects:
      org    = project["org"]
      number = project["number"]
      title  = project["title"]
      print(f"[cyan]Fetching items from: {title} (Org: {org}, Project: {number})[/cyan]")

      # Set the output path
      out_path:Path = Path(self.temp_dir,f"{org}-{number}.items.json")

      # use os.system instead of subprocess.run or subprocess.popen to avoid creating a new
      # process space where we would need to copy environment variables into it (possibly
      # exposing things like GH_TOKEN or other environment variables)
      os.system( f'gh project item-list --owner "{org}" {number} --format json > "{out_path}"')

      if not out_path.exists():
          print(f"[red]Failed to fetch items for project: {title} (Org: {org}, Project: {number})[/red]")
          rv = False

    return rv

  def consolidate_items(self) -> bool:
    """Consolidate all items into a single JSON file."""

    rv:bool = True
    all_items = []
    try:
      for file in self.temp_dir.glob("*.items.json"):
        with open(file) as f:
          data = json.load(f)
          items = data.get("items", [])
          all_items.extend(items)
    except Exception as e:
      print(f"[red]Error consolidating items: {e}[/red]")
      rv = False

    try:
      with open(self.output_file, "w") as f:
        json.dump(all_items, f, indent=2)
    except Exception as e:
      print(f"[red]Error writing consolidated items to {self.output_file}: {e}[/red]")
      rv = False

    if Path(self.output_file).exists():
      print(f"[bold green]Saved all items to {self.output_file}[/bold green]")
    return rv

  def cleanup(self) -> bool:
    """Cleanup temporary files."""
    rv = True
    if self.temp_dir.exists():
      try:
        shutil.rmtree(self.temp_dir)
        print(f"[bold purple]Cleaned up temporary files in {self.temp_dir}[/bold purple]")
      except Exception as e:
        print(f"[red]Error cleaning up temporary files: {e}[/red]")
        rv = False
    else:
      print(f"[bold green]No temporary files to clean up.[/bold green]")

    return rv

  def process(self) -> bool:
    """Main processing method for the Version2Query class."""

    if self.temp_dir.exists():
      self.cleanup()

    orgs = self.get_github_orgs()
    if not orgs:
      print("[red]No organizations found. Exiting...[/red]")
      return False

    all_projects = self.get_all_projects(orgs)
    if not all_projects:
      print("[red]No projects found. Exiting...[/red]")
      return False

    # filter by team names
    filtered_projects = all_projects
    if self.filters.include_teams is not None:
      teams = self.filters.include_teams
      filtered_projects_by_teams = self.filter_projects_by_team(all_projects, teams)
      if not filtered_projects_by_teams:
        print("[red]No projects found matching the team names. Exiting...[/red]")
        return False
      filtered_projects = filtered_projects_by_teams

    if not self.fetch_project_items(filtered_projects):
      print("[red]Failed to fetch project items. Exiting...[/red]")
      return False

    if not self.consolidate_items():
      print("[red]Failed to consolidate items. Exiting...[/red]")
      return False

    # filter items by user
    if self.filters.include_users is not None:
      self.filter_items_by_user()

    return self.cleanup()

# This main method is used for testing out the version2query class
def main():
  """The primary method for the version2query.py script."""
  project_names:list = input("Enter team name(s) to filter projects: ").split(",")
  test_temp_dir:Path = Path(f"tmp.dir")
  test_output_file:str = f"output.items.json"
  
  query = Version2Query(temp_dir=test_temp_dir, output_file=test_output_file)
  query.filters.include_projects = project_names
  if not query.process():
    print("[red]Processing failed.[/red]")
    raise RunTimeError("Processing failed.")

if __name__ == "__main__":
  main()
