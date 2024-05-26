from flask import Flask, render_template
from pathlib import Path

app = Flask(__name__, template_folder='./templates')


@app.route('/', methods=['GET'])
def index():
    title = Path(__file__).name
    book_name = 'hello world'
    return render_template('index5.html', **locals())


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
