"""
flask --app .\5-练习生成项目.py startapp home
> 项目`home`已生成，目录位于 D:\\study\\python-flask\\flask-demo\\day03\\home
"""

import os
import click
from flask import Flask

app = Flask(__name__)

config = {
    'project_name': 'default-app',
    'tree': [
        'views.py',
        {
            'static': None,
            'template': []
        },
        'models.py',
        'urls.py',
        'tests.py'
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
