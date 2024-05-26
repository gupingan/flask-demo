"""
flask --app .\5-练习生成项目.py --help
Usage: flask [OPTIONS] COMMAND [ARGS]...

  A general utility script for Flask applications.

  An application to load must be given with the '--app' option, 'FLASK_APP'
  environment variable, or with a 'wsgi.py' or 'app.py' file in the current
  directory.

Options:
  -e, --env-file FILE   Load environment variables from this file. python-
                        dotenv must be installed.
  -A, --app IMPORT      The Flask application or factory function to load, in
                        the form 'module:name'. Module can be a dotted import
                        or file path. Name is not required if it is 'app',
                        'application', 'create_app', or 'make_app', and can be
                        'name(args)' to pass arguments.
  --debug / --no-debug  Set debug mode.
  --version             Show the Flask version.
  --help                Show this message and exit.

Commands:
  routes    Show the routes for the app.
  run       Run a development server.
  shell     Run a shell in the app context.
  startapp  Crete a project.

flask --app .\5-练习生成项目.py startapp home
> 项目`home`已生成，目录位于 D:\\study\\python-flask\\flask-demo\\day03\\home
"""

import os
import click
from flask import Flask

app = Flask(__name__)

# config = {
#     'project_name': 'default-app',
#     'tree': [
#         'views.py',
#         {
#             'static': None,
#             'template': []
#         },
#         'models.py',
#         'urls.py',
#         'tests.py'
#     ]
# }

config = {
    'project_name': 'default-app',
    'tree': [
        ['views.py', 'models.py', 'urls.py', 'tests.py'],  # 和上方效果一致
        {
            'static': None,
            'template': []
        },
    ]
}


def generate():
    project_folder_name = config['project_name']
    os.makedirs(project_folder_name, exist_ok=True)

    def _operate(parent, node):
        if isinstance(node, str):
            path = os.path.join(parent, node)
            with open(path, 'w') as f:
                pass
        elif isinstance(node, dict):
            for folder, files in node.items():
                folder_path = os.path.join(parent, folder)
                os.makedirs(folder_path, exist_ok=True)
                if files is not None:
                    for file in files:
                        _operate(folder_path, file)
        elif isinstance(node, list):
            for item in node:
                _operate(parent, item)
        else:
            print(f'不支持 {type(node)} 类型')

    _operate(project_folder_name, config['tree'])


@app.cli.command('startapp')
@click.argument('project_name', type=str, default='default-app')
def startapp(project_name: str):
    """
    Crete a project.
    """
    config['project_name'] = project_name
    generate()
    print(f'> 项目`{project_name}`已生成，目录位于 {os.path.abspath(rf"./{project_name}")}')
