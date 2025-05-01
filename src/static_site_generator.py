from jinja2 import Environment, FileSystemLoader
import logging 


class StaticSiteGenerator():

    def __init__(self):
        self.GENERATOR_DATA = {
            'title': 'Version Two',
            'github_user': 'octocat',
            'team': 'Platform Engineering',
            'tasks': []
        }

    def generate_site(self, data=None, output_file='./_site/index.html'):
        logging.info("Generating Static Site")
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('kaban_board.html')

        self.GENERATOR_DATA["tasks"] = data if data is not None else []

        # Extract unique statuses from the tasks list
        unique_statuses = sorted({task["status"] for task in self.GENERATOR_DATA["tasks"]})
        
        # Add statuses to the data dictionary
        data_with_statuses = {**self.GENERATOR_DATA, "statuses": unique_statuses}
        
        # Render template with updated data
        output = template.render(data_with_statuses)
        
        with open(output_file, 'w') as f:
            f.write(output)

        logging.info("Static Site Generated @ ./_site/index.html")
