#!/usr/bin/env python3

import os
import json
import shutil
import requests
from pathlib import Path
from ghapi.all import GhApi
from rich import print

MYTEAM = "platform-ci"
TEMP_DIR = Path(f"{MYTEAM}.dir")
OUTPUT_FILE = f"{MYTEAM}.items.json"

# Create GitHub API client (assumes GITHUB_TOKEN is set in env)
api = GhApi()

# Step 1: Get list of orgs
orgs = [org["login"] for org in api.orgs.list_for_authenticated_user()]

# Step 2: Query projects for each org
all_projects = []
for org in orgs:
    print(f"[bold blue]Fetching projects for org: {org}[/bold blue]")

    query = """
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

    headers = {"Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"}
    response = requests.post(
        "https://api.github.com/graphql",
        json={"query": query, "variables": {"login": org}},
        headers=headers
    )
    result = response.json()
    projects = [
      {
        "org": org,
        "number": project["number"],
        "title": project["title"]
      }
      for project in result.get("data", {}).get("organization", {}).get("projectsV2", {}).get("nodes", [])
    ]

    all_projects.extend(projects)

# Step 3: Filter by team name in title
matching_projects = [
    p for p in all_projects if MYTEAM.lower() in p["title"].lower()
]

print(f"[green]Found {len(matching_projects)} matching projects for team '{MYTEAM}'[/green]")

# Step 4: Fetch items for each matching project
TEMP_DIR.mkdir(exist_ok=True)
for project in matching_projects:
    org = project["org"]
    number = project["number"]
    title = project["title"]

    print(f"[cyan]Fetching items from: {title} (Org: {org}, Project: {number})[/cyan]")

    # ghapi does not support the `gh project item-list` command yet,
    # so we use a subprocess call or GitHub REST if available.
    # We'll fallback to CLI for now.
    out_path = TEMP_DIR / f"{org}-{number}.items.json"
    os.system( f'gh project item-list --owner "{org}" {number} --format json > "{out_path}"')

# Step 5: Consolidate items
all_items = []
for file in TEMP_DIR.glob("*.items.json"):
    with open(file) as f:
        data = json.load(f)
        items = data.get("items", [])
        all_items.extend(items)

print(all_items)
with open(OUTPUT_FILE, "w") as f:
    json.dump(all_items, f, indent=2)

print(f"[bold green]Saved all items to {OUTPUT_FILE}[/bold green]")

# Step 6: Cleanup
shutil.rmtree(TEMP_DIR)
