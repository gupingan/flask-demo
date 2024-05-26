"""
# 显示路由
flask --app=.\day02\5-http-跳转页面.py routes
Endpoint  Methods    Rule
--------  ---------  -----------------------
index     GET, POST  /
jump      GET        /jump
login     GET        /login
static    GET        /static/<path:filename>

# 运行服务
flask --app=.\day02\5-http-跳转页面.py run
 * Serving Flask app '.\day02\5-http-跳转页面.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

# 终端交互
flask --app .\day03\1-请求全局钩子及其生命周期.py shell
Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
App: 1-请求全局钩子及其生命周期
Instance: D:\study\python-flask\flask-demo\day03\instance
>>> app
<Flask '1-请求全局钩子及其生命周期'>
"""
import click
from flask import Flask

app = Flask(__name__)


@app.cli.command('faker')
@click.argument('data', type=str, default='user')
@click.option('-n', '--number', 'number', type=int, default=1, help='生成的数据量')
def fake_command(data, number):
    """
    自定义命令
    """
    print(data, type(data))
    print(number, type(number))


"""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
> flask --app '.\4-flask 部分子命令.py' faker
user <class 'str'>
1 <class 'int'>


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
> flask --app '.\4-flask 部分子命令.py' faker ddd -n 1230
ddd <class 'str'>
1230 <class 'int'>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
> flask --app '.\4-flask 部分子命令.py' --help
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
  faker   自定义命令
  routes  Show the routes for the app.
  run     Run a development server.
  shell   Run a shell in the app context.
"""


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello Flask'


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
