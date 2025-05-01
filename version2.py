from src.version2config import VersionTwoConfig
from src.version2query import Version2Query
from src.static_site_generator import generate_site
from pathlib import Path
import json

def main():
    config:VersionTwoConfig = VersionTwoConfig()
    config.display_config()
    temp_dir:Path = Path(config.temp_dir)
    output_file:str = config.output_file
    teams:list[str] = config.include_team

    query:VersionTwoQuery = Version2Query(temp_dir=temp_dir, output_file=output_file)

    # Generate output_file or die
    if not query.process(teams):
      print("Failed to process query.")
      return

    # Get json object
    data = None
    with open(output_file, 'r') as f:
      data = json.load(f)

    generate_site(data=data)

if __name__ == "__main__":
    main()
