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
            # 个人建议仅存储 url，而不是 html，此处跟随课程所练习
            'cover': '<img src="./static/images/wmsj.webp"></img>'
        },
        {
            'id': 1003,
            'title': '吞噬星空',
            'author': '我吃西红柿',
            'price': 32.88,
            'cover': '<img src="./static/images/tsxk.webp"></img>'
        },
        {
            'id': 1004,
            'title': '星辰变',
            'author': '我吃西红柿',
            'price': 29.995,
            'cover': '<img src="./static/images/xcb.webp"></img>'
        },
        {
            'id': 1006,
            'title': '三国演义',
            'author': '罗贯中',
            'price': 39,
            'cover': '<img src="./static/images/sgyy.webp"></img>'
        },
        {
            'id': 1007,
            'title': '西游记',
            'author': '吴承恩',
            'price': 38.5,
            # 'cover': '<img src="./static/images/xyj.webp"></img>',
            'cover': '<script>alert("注入攻击")</script>'
        },
    ]
    return render_template('index4.html', **locals())


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
