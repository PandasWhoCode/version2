from jinja2 import Environment, FileSystemLoader

def generate_site(data, output_file='./_site/index.html'):
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
        ],
        'New': [
            {
                "assignees": [
                    "coolAssignee"
                ],
                "content": {
                    "body": "https://dummy_url/test#L42\n\nRename from `X` to `Y`",
                    "number": 241,
                    "repository": "pandas/coolrepo",
                    "title": "cool title",
                    "type": "Issue",
                    "url": "https://github.com/pandas/coolrepo/issues/241"
                },
                "id": "PVTI_lADOBgkjhkjhjjh",
                "labels": [
                    "Bug"
                ],
                "linked pull requests": [
                    "https://github.com/pandas/coolrepo/pull/242"
                ],
                "repository": "https://github.com/pandas/coolrepo",
                "status": "Done",
                "title": "Cool Pandas Task"
            }
        ],
        'In-Progress': [
        ],
        'Blocked': [
        ],
        'Done': [
        ]
    }
}


generate_site(data)
