from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
def index():
    title = '主页'
    content1 = 'This is a content1'
    content2 = 'Hi Flask'
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
