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




