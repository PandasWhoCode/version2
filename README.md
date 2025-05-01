![App icon](images/FullSizeIcon.png)

# VersionTwo
Hackathon project: CLI tool to generate static planning view of issues for better team planning

# 🚀 Getting Started
## 📦 Requirements
The following dependencies are required to run the program:
- Python 3.x
  - `brew install python3`
- Python `pyenv` and `pyenv-virtualenv`
  -  `brew install pyenv pyenv-virtualenv`
- GitHub Command Line Interface (CLI) `gh`
  - `brew install gh`

## 💻 Setup
- Authentication through `gh auth login`
- Set the appropriate token permissions: `gh auth refresh --scopes read:project`
  - Note: The team must be a member of the Project Board in order to view the issues on the board.
- Set the `GITHUB_TOKEN` environment variable: `export GITHUB_TOKEN=$(gh auth token)`
- Set the `GITHUB_UNAME` environment variable: `export GITHUB_UNAME=$(gh auth status | grep "(GITHUB_TOKEN)" | cut -d " " -f9)`
- Run `make install` inside the repo directory to configure the appropriate versions of dependencies.

## 🛠 Usage
To run the main script, change to the current directory of the script, then run:

`python version2.py --output-file "<filename.json>" --temp-dir "<temp.dir>" --include-team <teamname>`

See the `--help` menu for full list of filter functionality.

# Background
GitHub users have issues assigned to themselves or a team they are a member of. These issues can be viewed on a 
Project board, which captures the issues in swim lanes. The Project board can only automate with a single organization,
meaning users who work in more than one org do not have a single location to view all issues. This leads to fragmented
planning and execution.

# How does it work?

```mermaid
%% A · System-Architecture Diagram (≤25 nodes)
flowchart TD
    A[CLI Invocation] --> B{version2config.py<br/>Parse flags & env}
    B --> C[Validated Config]
    C --> D{version2query.py<br/>Token check}
    D --> E[GraphQL call projectsV2]:::api
    E --> F[gh project item-list]:::cli
    F --> G[items *.json]
    G --> H[Consolidate to output.items.json]
    H --> I{static_site_generator.py<br/>Jinja2 render}
    I --> J[_site/index.html]
classDef api fill:#e3f2fd,stroke:#2196f3;
classDef cli fill:#f1f8e9,stroke:#7cb342;
```

# Our Solution
Our python script will query the GitHub API for all issues associated with the appropriate filters provided to the CLI
tool. The output will be a static HTML page showing all issues in swim lanes. This provides a comprehensive overview
of all issues the team or user has assigned. 
