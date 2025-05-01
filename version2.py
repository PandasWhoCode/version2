from src.version2config import VersionTwoConfig
from src.version2query import VersionTwoQuery
from src.static_site_generator import generate_site


def main():
    config:VersionTwoConfig = VersionTwoConfig()
    config.display_config()
    temp_dir:Path = Path(config.temp_dir)
    output_file:str = config.output_file

    query:VersionTwoQuery = VersionTwoQuery(temp_dir=temp_dir, output_file=output_file)
    teams:list = input("Enter team name(s) to filter projects: ").split(",")

    # Generate output_file or die
    if not query.process(teams):
      print("Failed to process query.")
      return

    generate_site()

if __name__ == "__main__":
    main()
