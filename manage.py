from pathlib import Path
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    title = Path(__file__).name
    return 'Hello Flask'


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
