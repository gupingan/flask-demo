from flask import Flask

app = Flask(__name__)


@app.route(rule='/', methods=['GET', 'POST'])
def index():
    return 'Hello Flask'


# @app.route('/')
# def index():
#     return 'Hello Flask'

# @app.route('/')
# def index2():
#     return 'Hello Flask2'


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
