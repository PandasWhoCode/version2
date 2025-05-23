from jinja2 import Environment, FileSystemLoader
from rich import print
import json
import logging
import os


class StaticSiteGenerator():

    def __init__(self):
        self.GENERATOR_DATA:dict = {
            'title': 'Version2',
            'github_user': "",
            'project': "",
            'tasks': []
        }

    def generate_site(self, data:list=None, filter_done:bool=False, projects:list[str]=None, output_file='./_site/index.html') -> None:
        logging.info("Generating Static Site")
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('kaban_board.html')

        self.GENERATOR_DATA["tasks"] = data if data is not None else []

        # Set the github user name
        self.github_uname = os.getenv("GITHUB_UNAME") if os.getenv("GITHUB_UNAME") else "Not logged in"
        self.GENERATOR_DATA["github_user"] = self.github_uname

        # Set the project(s)
        self.GENERATOR_DATA["project"] = ' '.join(projects) if projects is not None else ""

        # Ensure all tasks have a status
        statuses:set[str] = set()
        for task in self.GENERATOR_DATA["tasks"]:
            if "status" not in task:
              task["status"] = "NONE"
            elif task["status"].upper() == "DONE" and filter_done == True:
                # remove the task from the list
                self.GENERATOR_DATA["tasks"].remove(task)
                continue
            else:
              task["status"] = task["status"].upper()
            statuses.add(task["status"])
        print(f"[bold cyan]Adding {len(self.GENERATOR_DATA["tasks"])} tasks to the site[/bold cyan]")

        # Extract unique statuses from the tasks list
        unique_statuses:list[str] = sorted(statuses)

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

