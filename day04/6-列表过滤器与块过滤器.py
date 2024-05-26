from flask import Flask, render_template
from pathlib import Path

app = Flask(__name__, template_folder='./templates')


@app.route('/', methods=['GET'])
def index():
    title = Path(__file__).name
    # 以下books为虚假数据，仅供案例
    books = [
        {
            'id': 1001,
            'title': '完美世界',
            'author': '辰东',
            'price': 29.355,
            'cover': './static/images/wmsj.webp'
        },
        {
            'id': 1003,
            'title': '吞噬星空',
            'author': '我吃西红柿',
            'price': 32.88,
            'cover': './static/images/tsxk.webp'
        },
        {
            'id': 1004,
            'title': '星辰变',
            'author': '我吃西红柿',
            'price': 29.995,
            'cover': './static/images/xcb.webp'
        },
        {
            'id': 1006,
            'title': '三国演义',
            'author': '罗贯中',
            'price': 39,
            'cover': './static/images/sgyy.webp'
        },
        {
            'id': 1007,
            'title': '西游记',
            'author': '吴承恩',
            'price': 38.5,
            'cover': './static/images/xyj.webp'
        },
    ]
    return render_template('index6.html', **locals())


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
