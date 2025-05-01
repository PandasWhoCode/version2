from jinja2 import Environment, FileSystemLoader
import json 

# Example data
GENERATOR_DATA = {
    'title': 'Version Two',
    'github_user': 'octocat',
    'team': 'Platform Engineering',
    'tasks': []
}

def generate_site(data=None, output_file='./_site/index.html'):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('kaban_board.html')

    GENERATOR_DATA["tasks"] = data if data is not None else []

    # Extract unique statuses from the tasks list
    unique_statuses = sorted({task["status"] for task in GENERATOR_DATA["tasks"]})
    
    # Add statuses to the data dictionary
    data_with_statuses = {**GENERATOR_DATA, "statuses": unique_statuses}
    
    # Render template with updated data
    output = template.render(data_with_statuses)
    
    with open(output_file, 'w') as f:
        f.write(output)

