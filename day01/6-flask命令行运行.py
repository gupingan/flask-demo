from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/welcome')
def welcome():
    return '<h1>你好，Flask</h1>'


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)

# 命令行运行
"""
$env:FLASK_DEBUG=1
$env:FLASK_APP=".\day01\6-flask命令行运行.py"
flask run --host=0.0.0.0 --port=8888
或者
flask --app hello run --debug
"""
