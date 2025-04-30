from jinja2 import Environment, FileSystemLoader

def render_kanban_board(data, output_file='./_site/index.html'):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('kaban_board.html')
    output = template.render(data)
    
    with open(output_file, 'w') as f:
        f.write(output)

# Example data
data = {
    'title': 'Version Two',
    'github_user': 'octocat',
    'team': 'Platform Engineering',
    'tasks': {
        'Backlog': [
            {'title': 'Research competitors', 'description': 'Analyze feature set'},
            {'title': 'Set up project repo', 'description': 'Initialize GitHub repo'},
        ],
        'New': [
            {'title': 'Design wireframes', 'description': 'Homepage + Dashboard'},
        ],
        'In-Progress': [
            {'title': 'Implement auth', 'description': 'Login + Register'},
        ],
        'Blocked': [
            {'title': 'API integration', 'description': 'Waiting for backend team'},
        ],
        'Done': [
            {'title': 'Project kickoff', 'description': 'Team intro & planning'},
        ]
    }
}


render_kanban_board(data)
