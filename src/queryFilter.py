"""
query_filter.py

This module defines the QueryFilter class, which is used to filter GitHub projects based on various criteria.
It is used in the Version2Query class to filter projects based on user input.
"""

from rich import print

class QueryFilter:
  # the def method takes in a list of strings for each filter type
  def __init__(
    self,
    include_projects:list[str]=None,
    include_users:list[str]=None,
    include_repositories:list[str]=None,
    include_organizations:list[str]=None,
    include_organization_repositories:list[str]=None,
    include_labels:list[str]=None,
    include_teams:list[str]=None,
    exclude_projects:list[str]=None,
    exclude_users:list[str]=None,
    exclude_repositories:list[str]=None,
    exclude_organizations:list[str]=None,
    exclude_organization_repositories:list[str]=None,
    exclude_label:list[str]=None,
    exclude_teams:list[str]=None
  ):
    self.include_projects:list[str]                  = include_projects
    self.include_users:list[str]                     = include_users
    self.include_repositories:list[str]              = include_repositories
    self.include_organizations:list[str]             = include_organizations
    self.include_organization_repositories:list[str] = include_organization_repositories
    self.include_labels:list[str]                    = include_labels
    self.include_teams:list[str]                     = include_teams
    self.exclude_projects:list[str]                  = exclude_projects
    self.exclude_users:list[str]                     = exclude_users
    self.exclude_repositories:list[str]              = exclude_repositories
    self.exclude_organizations:list[str]             = exclude_organizations
    self.exclude_organization_repositories:list[str] = exclude_organization_repositories
    self.exclude_label:list[str]                     = exclude_label
    self.exclude_teams:list[str]                     = exclude_teams

  @property
  def include_projects(self) -> list[str]:
    return self._include_projects
  @include_projects.setter
  def include_projects(self, value:list[str]) -> None:
    self._include_projects=value

  @property
  def include_users(self) -> list[str]:
    return self._include_users
  @include_users.setter
  def include_users(self, value:list[str]) -> None:
    self._include_users=value

  @property
  def include_repositories(self) -> list[str]:
    return self._include_repositories
  @include_repositories.setter
  def include_repositories(self, value:list[str]) -> None:
    self._include_repositories=value

  @property
  def include_organizations(self) -> list[str]:
    return self._include_organizations
  @include_organizations.setter
  def include_organizations(self, value:list[str]) -> None:
    self._include_organizations=value

  @property
  def include_organization_repositories(self) -> list[str]:
    return self._include_organization_repositories
  @include_organization_repositories.setter
  def include_organization_repositories(self, value:list[str]) -> None:
    self._include_organization_repositories=value

  @property
  def include_labels(self) -> list[str]:
    return self._include_labels
  @include_labels.setter
  def include_labels(self, value:list[str]) -> None:
    self._include_labels=value

  @property
  def include_teams(self) -> list[str]:
    return self._include_teams
  @include_teams.setter
  def include_teams(self, value:list[str]) -> None:
    self._include_teams=value

  @property
  def exclude_projects(self) -> list[str]:
    return self._exclude_projects
  @exclude_projects.setter
  def exclude_projects(self, value:list[str]) -> None:
    self._exclude_projects=value

  @property
  def exclude_users(self) -> list[str]:
    return self._exclude_users
  @exclude_users.setter
  def exclude_users(self, value:list[str]) -> None:
    self._exclude_users=value

  @property
  def exclude_repositories(self) -> list[str]:
    return self._exclude_repositories
  @exclude_repositories.setter
  def exclude_repositories(self, value:list[str]) -> None:
    self._exclude_repositories=value

  @property
  def exclude_organizations(self) -> list[str]:
    return self._exclude_organizations
  @exclude_organizations.setter
  def exclude_organizations(self, value:list[str]) -> None:
    self._exclude_organizations=value

  @property
  def exclude_organization_repositories(self) -> list[str]:
    return self._exclude_organization_repositories
  @exclude_organization_repositories.setter
  def exclude_organization_repositories(self, value:list[str]) -> None:
    self._exclude_organization_repositories=value

  @property
  def exclude_label(self) -> list[str]:
    return self._exclude_label
  @exclude_label.setter
  def exclude_label(self, value:list[str]) -> None:
    self._exclude_label=value

  @property
  def exclude_teams(self) -> list[str]:
    return self._exclude_teams
  @exclude_teams.setter
  def exclude_teams(self, value:list[str]) -> None:
    self._exclude_teams=value

  def print_filters(self) -> None:
    """Print the filters for debugging purposes."""
    print(f"[bold green]Filters:[/bold green]")
    print(f"Include Projects: {self.include_projects}")
    print(f"Include Users: {self.include_users}")
    print(f"Include Repositories: {self.include_repositories}")
    print(f"Include Organizations: {self.include_organizations}")
    print(f"Include Organization Repositories: {self.include_organization_repositories}")
    print(f"Include Labels: {self.include_labels}")
    print(f"Include Teams: {self.include_teams}")
    print(f"Exclude Projects: {self.exclude_projects}")
    print(f"Exclude Users: {self.exclude_users}")
    print(f"Exclude Repositories: {self.exclude_repositories}")
    print(f"Exclude Organizations: {self.exclude_organizations}")
    print(f"Exclude Organization Repositories: {self.exclude_organization_repositories}")
    print(f"Exclude Label: {self.exclude_label}")
    print(f"Exclude Teams: {self.exclude_teams}")

  def get_filters(self) -> dict[str,list[str]]:
    """Get the filters as a dictionary."""
    return {
      "include_projects":                  self.include_projects,
      "include_users":                     self.include_users,
      "include_repositories":              self.include_repositories,
      "include_organizations":             self.include_organizations,
      "include_organization_repositories": self.include_organization_repositories,
      "include_labels":                    self.include_labels,
      "include_teams":                     self.include_teams,
      "exclude_projects":                  self.exclude_projects,
      "exclude_users":                     self.exclude_users,
      "exclude_repositories":              self.exclude_repositories,
      "exclude_organizations":             self.exclude_organizations,
      "exclude_organization_repositories": self.exclude_organization_repositories,
      "exclude_label":                     self.exclude_label,
      "exclude_teams":                     self.exclude_teams
    }

  def set_filters_from_dict(self, filters:dict[str,list[str]]):
    """Set the filters from a dictionary."""
    self.include_projects                  = filters.get("include_projects", [])
    self.include_users                     = filters.get("include_users", [])
    self.include_repositories              = filters.get("include_repositories", [])
    self.include_organizations             = filters.get("include_organizations", [])
    self.include_organization_repositories = filters.get("include_organization_repositories", [])
    self.include_labels                    = filters.get("include_labels", [])
    self.include_teams                     = filters.get("include_teams", [])
    self.exclude_projects                  = filters.get("exclude_projects", [])
    self.exclude_users                     = filters.get("exclude_users", [])
    self.exclude_repositories              = filters.get("exclude_repositories", [])
    self.exclude_organizations             = filters.get("exclude_organizations", [])
    self.exclude_organization_repositories = filters.get("exclude_organization_repositories", [])
    self.exclude_label                     = filters.get("exclude_label", [])
    self.exclude_teams                     = filters.get("exclude_teams", [])
