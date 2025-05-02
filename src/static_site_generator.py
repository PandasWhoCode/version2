from jinja2 import Environment, FileSystemLoader
from rich import print
import json
import logging
import os


class StaticSiteGenerator():

    def __init__(self):
        self.GENERATOR_DATA = {
            'title': 'Version2',
            'github_user': "",
            'project': "",
            'tasks': []
        }

    def generate_site(self, data:list=None, projects:list[str]=None, output_file='./_site/index.html') -> None:
        logging.info("Generating Static Site")
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('kaban_board.html')

        self.GENERATOR_DATA["tasks"] = data if data is not None else []

        # Set the github user name
        self.github_uname = os.getenv("GITHUB_UNAME") if os.getenv("GITHUB_UNAME") else "Not logged in"
        self.GENERATOR_DATA["github_user"] = self.github_uname

        # Set the project(s)
        self.GENERATOR_DATA["project"] = ' '.join(projects) if projects is not None else ""

        # Extract unique statuses from the tasks list
        statuses:list[str] = []
        for task in self.GENERATOR_DATA["tasks"]:
            if "status" in task:
                statuses.append(task["status"])
        unique_statuses:list[str] = sorted(set(statuses))

        # Add statuses to the data dictionary
        data_with_statuses = {**self.GENERATOR_DATA, "statuses": unique_statuses}
        
        # Render template with updated data
        output = template.render(data_with_statuses)
        
        with open(output_file, 'w') as f:
            f.write(output)

        logging.info("Static Site Generated @ ./_site/index.html")

def main():
    ss_gen = StaticSiteGenerator()
    data_file:str = input("Enter the path to the json file with data: ")
    if not os.path.exists(data_file):
        print(f"[bold red]File {data_file} does not exist.[/bold red]")
        return

    data:list = []
    with open(data_file, 'r') as f:
        data = json.load(f)

    ss_gen.generate_site(data=data)

if __name__ == "__main__":
    main()

