from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/welcome')
def welcome():
    return '<h1>你好，Flask</h1>'


def demo():
    return '<h3>你好，Demo</h3>'


# app.route('/demo')(demo)
app.add_url_rule('/demo', None, demo)

if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
    # from werkzeug import run_simple

    # run_simple('0.0.0.0', 9527, app, use_reloader=True, use_debugger=True)
    # debug=True  <==> use_reloader=True, use_debugger=True
