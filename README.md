![App icon](images/FullSizeIcon.png)

# VersionTwo
Hackathon project: CLI tool to generate static planning view of issues for better team planning

# Problem we are solving
GitHub projects users are unable to easily associate issues across organizations with a project and particularly find having to manually add issues to the project board itself as a time consuming unnecessarily difficult task.

We propose improving this interface by adding a simple HTTP page with an interactive Kanban which is able to aggregate a user provided selection of repos, projects, organizations and display them in a filterable way.

# Getting Started
## Requirements and Setup
The following items are required to run the program.
- Python 3.x
- Python `pyenv` and `pyenv-virtualenv`
  -  `brew install pyenv pyenv-virtualenv`
- GitHub Command Line Interface (CLI) `gh`
- Authentication through `gh auth login`

Run `make install` inside the repo directory to configure the appropriate versions of dependencies.

