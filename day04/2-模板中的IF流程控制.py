import random
from pathlib import Path
from flask import Flask, render_template, session

app = Flask(__name__, template_folder='./templates')

app.secret_key = 'my secret key'


@app.route('/', methods=['GET'])
def index():
    title = Path(__file__).name
    age = random.randint(0, 100)
    session['score'] = random.randint(-18, 118)
    return render_template('index2.html', **locals())


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
