from jinja2 import Environment, FileSystemLoader

# Example data
dummy_data = {
    'title': 'Version Two',
    'github_user': 'octocat',
    'team': 'Platform Engineering',
    'tasks': [
        {
            "assignees": ["coolAssignee"],
            "content": {
                "body": "https://dummy_url/test#L42\n\nRename from `X` to `Y`",
                "number": 241,
                "repository": "pandas/coolrepo",
                "title": "cool title",
                "type": "Issue",
                "url": "https://github.com/pandas/coolrepo/issues/241"
            },
            "id": "PVTI_lADOBgkjhkjhjjh",
            "labels": ["Bug"],
            "linked pull requests": ["https://github.com/pandas/coolrepo/pull/242"],
            "repository": "https://github.com/pandas/coolrepo",
            "status": "New",
            "title": "Cool Pandas Task 1"
        },
        {
            "assignees": ["coolAssignee"],
            "content": {
                "body": "https://dummy_url/test#L42\n\nRename from `X` to `Y`",
                "number": 241,
                "repository": "pandas/coolrepo",
                "title": "cool title",
                "type": "Issue",
                "url": "https://github.com/pandas/coolrepo/issues/241"
            },
            "id": "PVTI_lADOBgkjhkjhjjh",
            "labels": ["Bug"],
            "linked pull requests": ["https://github.com/pandas/coolrepo/pull/242"],
            "repository": "https://github.com/pandas/coolrepo",
            "status": "Backlog",
            "title": "Cool Pandas Task 2"
        },
        {
            "assignees": ["coolAssignee"],
            "content": {
                "body": "https://dummy_url/test#L42\n\nRename from `X` to `Y`",
                "number": 241,
                "repository": "pandas/coolrepo",
                "title": "cool title",
                "type": "Issue",
                "url": "https://github.com/pandas/coolrepo/issues/241"
            },
            "id": "PVTI_lADOBgkjhkjhjjh",
            "labels": ["Bug"],
            "linked pull requests": ["https://github.com/pandas/coolrepo/pull/242"],
            "repository": "https://github.com/pandas/coolrepo",
            "status": "In Progress",
            "title": "Cool Pandas Task 3"
        },
        {
            "assignees": ["coolAssignee"],
            "content": {
                "body": "https://dummy_url/test#L42\n\nRename from `X` to `Y`",
                "number": 241,
                "repository": "pandas/coolrepo",
                "title": "cool title",
                "type": "Issue",
                "url": "https://github.com/pandas/coolrepo/issues/241"
            },
            "id": "PVTI_lADOBgkjhkjhjjh",
            "labels": ["Bug"],
            "linked pull requests": ["https://github.com/pandas/coolrepo/pull/242"],
            "repository": "https://github.com/pandas/coolrepo",
            "status": "Blocked",
            "title": "Cool Pandas Task 4"
        },
        {
            "assignees": ["coolAssignee"],
            "content": {
                "body": "https://dummy_url/test#L42\n\nRename from `X` to `Y`",
                "number": 241,
                "repository": "pandas/coolrepo",
                "title": "cool title",
                "type": "Issue",
                "url": "https://github.com/pandas/coolrepo/issues/241"
            },
            "id": "PVTI_lADOBgkjhkjhjjh",
            "labels": ["Bug"],
            "linked pull requests": ["https://github.com/pandas/coolrepo/pull/242"],
            "repository": "https://github.com/pandas/coolrepo",
            "status": "Done",
            "title": "Cool Pandas Task 5"
        }
    ]
}

def generate_site(data=dummy_data, output_file='./_site/index.html'):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('kaban_board.html')
    
    # Extract unique statuses from the tasks list
    unique_statuses = sorted({task["status"] for task in data["tasks"]})
    
    # Add statuses to the data dictionary
    data_with_statuses = {**data, "statuses": unique_statuses}
    
    # Render template with updated data
    output = template.render(data_with_statuses)
    
    with open(output_file, 'w') as f:
        f.write(output)

