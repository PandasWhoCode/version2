#!/usr/bin/env python3

import os
import json
import shutil
import requests
from pathlib import Path
from ghapi.all import GhApi
from rich import print

TEMP_DIR = Path(f"tmp.dir")
OUTPUT_FILE = f"output.items.json"

def get_github_token():
  """Get GitHub token from environment variable."""
  token = os.getenv("GITHUB_TOKEN")
  if not token:
    raise ValueError("GITHUB_TOKEN environment variable is not set.")
  return token

def get_github_orgs():
  """Create a list of github orgs based on the authenticated user."""

  # Create the Github API
  api:GhApi = GhApi()

  # Grab the orgs:
  orgs:list[str] = [org["login"] for org in api.orgs.list_for_authenticated_user()]

  return orgs

def get_all_projects(orgs:list[str]) -> list[dict]:
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

    headers:dict = {"Authorization": f"Bearer {get_github_token()}"}
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

def projects_filtered_by_team(project_list:list[dict], teams:list[str]) -> list[dict]:
  """Filter the project list by team names."""

  filtered_projects:list[dict] = []
  for team in teams:
    matching_projects:list[dict] = [
      p for p in project_list if team.lower() in p["title"].lower()
    ]

    filtered_projects.extend(matching_projects)
    print(f"[green]Found {len(matching_projects)} matching projects for team '{team}'[/green]")
  return filtered_projects

def get_items_for_projects(projects:list[dict]) -> bool:
   """Fetch all items on each project."""
   
   rv:bool = True
   TEMP_DIR.mkdir(exist_ok=True)
   for project in projects:
    org    = project["org"]
    number = project["number"]
    title  = project["title"]
    print(f"[cyan]Fetching items from: {title} (Org: {org}, Project: {number})[/cyan]")

    # Set the output path
    out_path:Path = Path(TEMP_DIR,f"{org}-{number}.items.json")

    # use os.system instead of subprocess.run or subprocess.popen to avoid creating a new
    # process space where we would need to copy environment variables into it (possibly
    # exposing things like GH_TOKEN or other environment variables)
    os.system( f'gh project item-list --owner "{org}" {number} --format json > "{out_path}"')

    if not out_path.exists():
        print(f"[red]Failed to fetch items for project: {title} (Org: {org}, Project: {number})[/red]")
        rv = False
        continue
    
    return rv

def consolidate_items() -> bool:
  """Consolidate all items into a single JSON file."""
  
  rv:bool = True
  all_items = []
  try:
    for file in TEMP_DIR.glob("*.items.json"):
      with open(file) as f:
        data = json.load(f)
        items = data.get("items", [])
        all_items.extend(items)
  except Exception as e:
    print(f"[red]Error consolidating items: {e}[/red]")
    rv = False

  try:
    with open(OUTPUT_FILE, "w") as f:
      json.dump(all_items, f, indent=2)
  except Exception as e:
    print(f"[red]Error writing consolidated items to {OUTPUT_FILE}: {e}[/red]")
    rv = False

  if OUTPUT_FILE.exists():
    print(f"[bold green]Saved all items to {OUTPUT_FILE}[/bold green]")
  return rv

def cleanup() -> bool:
  """Cleanup temporary files."""
  rv = True
  if TEMP_DIR.exists():
    try:
      shutil.rmtree(TEMP_DIR)
      print(f"[bold red]Cleaned up temporary files in {TEMP_DIR}[/bold red]")
    except Exception as e:
      print(f"[red]Error cleaning up temporary files: {e}[/red]")
      rv = False
  else:
    print(f"[bold green]No temporary files to clean up.[/bold green]")
  
  return rv

def main():
  """The primary method for the version2query.py script."""
  teams:list = input("Enter team name(s) to filter projects: ").split(" ")
  
  if not teams:
    print("[red]No team names provided. Exiting...[/red]")
    return
  
  orgs = get_github_orgs()
  if not orgs:
    print("[red]No organizations found. Exiting...[/red]")
    return
  
  all_projects = get_all_projects(orgs)
  if not all_projects:
    print("[red]No projects found. Exiting...[/red]")
    return
  
  filtered_projects = projects_filtered_by_team(all_projects, teams)
  if not filtered_projects:
    print("[red]No projects found for the specified teams. Exiting...[/red]")
    return
  
  if not get_items_for_projects(filtered_projects):
    print("[red]Failed to fetch items for projects. Exiting...[/red]")
    return
  
  if not consolidate_items():
    print("[red]Failed to consolidate items. Exiting...[/red]")
    return
  
  cleanup()
