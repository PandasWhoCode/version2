from jinja2 import Environment, FileSystemLoader
import json 

# Example data
seed_data = {
    'title': 'Version2',
    'github_user': 'octocat',
    'team': 'Platform Engineering',
    'tasks': []
}

def generate_site(output_file='./_site/index.html'):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('kaban_board.html')
    with open('output.items.json', 'r') as file:
        gh_json = json.load(file)


    seed_data["tasks"] = gh_json

    # Extract unique statuses from the tasks list
    unique_statuses = sorted({task["status"] for task in seed_data["tasks"]})
    
    # Add statuses to the data dictionary
    data_with_statuses = {**seed_data, "statuses": unique_statuses}
    
    # Render template with updated data
    output = template.render(data_with_statuses)
    
    with open(output_file, 'w') as f:
        f.write(output)

