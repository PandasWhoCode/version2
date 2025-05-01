from src.version2config import VersionTwoConfig
from src.static_site_generator import generate_site


def main():
    config = VersionTwoConfig()
    config.display_config()

    generate_site()

if __name__ == "__main__":
    main()
