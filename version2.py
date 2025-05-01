from src.version2config import VersionTwoConfig
from src.version2query import Version2Query
from src.static_site_generator import StaticSiteGenerator
from pathlib import Path
import json
import logging

def main():
    config:VersionTwoConfig = VersionTwoConfig()
    config.display_config()
    temp_dir:Path = Path(config.temp_dir)
    output_file:str = config.output_file

    # Get parameters for filters
    filters:dict[str,list[str]] = {
      "include_teams":                     config.include_team,
      "include_users":                     config.include_user,
      "include_repositories":              config.include_repository,
      "include_organizations":             config.include_organization,
      "include_organization_repositories": config.include_organization_repository,
      "include_labels":                    config.include_label,
      "exclude_teams":                     config.exclude_team,
      "exclude_users":                     config.exclude_user,
      "exclude_repositories":              config.exclude_repository,
      "exclude_organizations":             config.exclude_organization,
      "exclude_organization_repositories": config.exclude_organization_repository,
      "exclude_label":                     config.exclude_label
    }

    query:VersionTwoQuery = Version2Query(temp_dir=temp_dir, output_file=output_file)
    ss_gen = StaticSiteGenerator()

    # Set filters
    query.set_filters(filters=filters)

    # Generate output_file or die
    logging.info("Querying GitHub API...")
    if not query.process():
      logging.error("Failed to process query.")
      return

    # Get json object
    data = None
    with open(output_file, 'r') as f:
      data = json.load(f)

    ss_gen.generate_site(data=data)

if __name__ == "__main__":
    main()
