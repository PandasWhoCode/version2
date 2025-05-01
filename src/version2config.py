import argparse
import logging
import os

class VersionTwoConfig:
    
    # LOGGER VARIABLES
    LOG_LEVEL = logging.INFO
    LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

    def __init__(self):
        self.init_parser()
        self.init_logger()
        self.load_env()

    def init_parser(self):
        parser = argparse.ArgumentParser(
            prog='VersionTwo',
            description="Render an HTML page from a collection of GitHub Issues and Pull Requests"
        )

        parser.add_argument(
            "--output-file",
            dest="output_file",
            action="store",
            type=str,
            default="output.projects.json",
            help="The output file to write the json data to"
        )

        parser.add_argument(
          "--temp-dir",
          dest="temp_dir",
          action="store",
          type=str,
          default="tmp.dir",
          help="The temporary directory to store the json data files"
        )

        parser.add_argument(
            "--include-team",
            dest="include_team",
            action="append",
            type=str,
            help="Include provided teams in the output"
        )

        parser.add_argument(
            "--include-user",
            dest="include_user",
            action="append",
            type=str,
            help="Include all issues and PRs for the provided user [Required Parameter]"
        )

        parser.add_argument(
            "--include-repository",
            dest="include_repository",
            action="append",
            type=str,
            help="Include all issues and PRs from the specified repository"
        )

        parser.add_argument(
            "--include-organization",
            dest="include_organization",
            action="append",
            type=str,
            help="Include all issues and PRs from the specified organization"
        )

        parser.add_argument(
            "--include-organization-repository",
            dest="include_organization_repository",
            action="append",
            type=str,
            help="Include all issues and PRs from the specified organization/repository"
        )

        parser.add_argument(
            "--include-label",
            dest="include_label",
            action="append",
            type=str,
            help="Include all issues and PRs with the specified label"
        )

        parser.add_argument(
            "--exclude-team",
            dest="exclude_team",
            action="append",
            type=str,
            help="Exclude provided teams in the output"
        )

        parser.add_argument(
            "--exclude-user",
            dest="exclude_user",
            action="append",
            type=str,
            help="Exclude all issues and PRs for the provided user"
        )

        parser.add_argument(
            "--exclude-repository",
            dest="exclude_repository",
            action="append",
            type=str,
            help="Exclude all issues and PRs from the specified repository"
        )

        parser.add_argument(
            "--exclude-organization",
            dest="exclude_organization",
            action="append",
            type=str,
            help="Exclude all issues and PRs from the specified organization"
        )

        parser.add_argument(
            "--exclude-organization-repository",
            dest="exclude_organization_repository",
            action="append",
            type=str,
            help="Exclude all issues and PRs from the specified "
                 "organization/repository"
        )

        parser.add_argument(
            "--exclude-label",
            dest="exclude_label",
            action="append",
            type=str,
            help="Exclude all issues and PRs with the specified label"
        )

        parser.add_argument(
            "--publish-board",
            dest="publish_board",
            action="store_const",
            help="The organization/board to publish (add) the collection of GitHub Issues and Pull Requests"
        )

        parsed_args = parser.parse_args()

        self.output_file = parsed_args.output_file
        self.temp_dir = parsed_args.temp_dir
        self.include_team = parsed_args.include_team
        self.include_user = parsed_args.include_user
        self.include_repository = parsed_args.include_repository
        self.include_organization = parsed_args.include_organization
        self.include_organization_repository = parsed_args.include_organization_repository
        self.include_label = parsed_args.include_label
        self.exclude_team = parsed_args.exclude_team
        self.exclude_user = parsed_args.exclude_user
        self.exclude_repository = parsed_args.exclude_repository
        self.exclude_organization = parsed_args.exclude_organization
        self.exclude_organization_repository = parsed_args.exclude_organization_repository
        self.exclude_label = parsed_args.exclude_label
        self.publish_board = parsed_args.publish_board

    def init_logger(self):
        logging.basicConfig(level=self.LOG_LEVEL, format=self.LOG_FORMAT)
    
    def load_env(self):
        self.GITHUB_PAT = os.getenv("GITHUB_PAT") if os.getenv("GITHUB_PAT") else None

    def display_config(self):
        logging.info("Configuration:")
        logging.info(f"Output File: {self.output_file}")
        logging.info(f"Temporary Directory: {self.temp_dir}")
        logging.info(f"Include Team: {self.include_team}")
        logging.info(f"Include User: {self.include_user}")
        logging.info(f"Include Repository: {self.include_repository}")
        logging.info(f"Include Organization: {self.include_organization}")
        logging.info(f"Include Organization/Repository: {self.include_organization_repository}")
        logging.info(f"Include Label: {self.include_label}")
        logging.info(f"Exclude Team: {self.exclude_team}")
        logging.info(f"Exclude User: {self.exclude_user}")
        logging.info(f"Exclude Repository: {self.exclude_repository}")
        logging.info(f"Exclude Organization: {self.exclude_organization}")
        logging.info(f"Exclude Organization/Repository: {self.exclude_organization_repository}")
        logging.info(f"Exclude Label: {self.exclude_label}")
        logging.info(f"Publish Board: {self.publish_board}")
