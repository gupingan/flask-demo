import json
from flask import Flask, request, make_response, Response, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello Flask', 200, {'Content-Type': 'flask'}


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
