from pathlib import Path
from flask import Flask, render_template
from filters import filters

app = Flask(__name__, template_folder='./templates')

for name, callback in filters.items():
    app.add_template_filter(callback, name)


@app.route('/', methods=['GET'])
def index():
    title = Path(__file__).name
    return render_template('index7.html', **locals())


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
