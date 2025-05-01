import argparse


class VersionTwoConfig:
    def __init__(self):
        parser = argparse.ArgumentParser(
            prog='VersionTwo',
            description="Render an HTML page from a collection of GitHub Issues"
                        "and Pull Requests",
        )

        parser.add_argument(
            "--include-organization",
            dest="include_org",
            action="append_const",
            help="Include all issues and PRs from the specified organization",)

        parser.add_argument(
            "--include-repository",
            dest="include_repository",
            action="append_const",
            help="Include all issues and PRs from the specified repository",)

        parser.add_argument(
            "--include-organization-repository",
            dest="include_organization_repository",
            action="append_const",
            help="Include all issues and PRs from the specified "
                 "organization/repository",)

        parser.add_argument(
            "--include-user",
            dest="include_user",
            action="append_const",
            help="Include all issues and PRs for the provided user",)

        parser.add_argument(
            "--include-label",
            dest="include_label",
            action="append_const",
            help="Include all issues and PRs with the specified label",)

        parser.add_argument(
            "--exclude-organization",
            dest="include_org",
            action="append_const",
            help="Exclude all issues and PRs from the specified organization",)

        parser.add_argument(
            "--exclude-repository",
            dest="include_repository",
            action="append_const",
            help="Exclude all issues and PRs from the specified repository",)

        parser.add_argument(
            "--exclude-organization-repository",
            dest="include_organization_repository",
            action="append_const",
            help="Exclude all issues and PRs from the specified "
                 "organization/repository",)

        parser.add_argument(
            "--exclude-user",
            dest="include_user",
            action="append_const",
            help="Exclude all issues and PRs for the provided user",)

        parser.add_argument(
            "--exclude-label",
            dest="include_label",
            action="append_const",
            help="Exclude all issues and PRs with the specified label",)

        parser.add_argument(
            "--publish-board",
            dest="publish_board",
            action="append_const",
            help="The organization/board to publish (add) the collection of "
                 "GitHub Issues and Pull Requests",)

        parsed_args = parser.parse_args()

        self.include_org = parsed_args.include_org
        self.include_repository = parsed_args.include_repository
        self.include_organization_repository = parsed_args.include_organization_repository
        self.include_user = parsed_args.include_user
        self.include_label = parsed_args.include_label
        self.exclude_org = parsed_args.exclude_org
        self.exclude_repository = parsed_args.exclude_repository
        self.exclude_organization_repository = parsed_args.exclude_organization_repository
        self.exclude_user = parsed_args.exclude_user
        self.exclude_label = parsed_args.exclude_label
        self.publish_board = parsed_args.publish_board

    def display_config(self):
        print("Configuration:")
        print(f"Include Organization: {self.include_org}")
        print(f"Include Repository: {self.include_repository}")
        print(f"Include Organization/Repository: {self.include_organization_repository}")
        print(f"Include User: {self.include_user}")
        print(f"Include Label: {self.include_label}")
        print(f"Exclude Organization: {self.exclude_org}")
        print(f"Exclude Repository: {self.exclude_repository}")
        print(f"Exclude Organization/Repository: {self.exclude_organization_repository}")
        print(f"Exclude User: {self.exclude_user}")
        print(f"Exclude Label: {self.exclude_label}")
        print(f"Publish Board: {self.publish_board}")


