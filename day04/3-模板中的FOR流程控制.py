from flask import Flask, render_template
from pathlib import Path

app = Flask(__name__, template_folder='./templates')


@app.route('/', methods=['GET'])
def index():
    title = Path(__file__).name
    fans = [
        {
            'id': 1001,
            'name': '小王',
            'age': 18,
        },
        {
            'id': 1003,
            'name': '老王',
            'age': 32,
        },
        {
            'id': 1004,
            'name': '金庸',
            'age': 29,
        },
        {
            'id': 1006,
            'name': '消炎',
            'age': 39,
        },
        {
            'id': 1007,
            'name': '陆风',
            'age': 18,
        },
    ]
    return render_template('index3.html', **locals())


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
