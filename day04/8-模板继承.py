from pathlib import Path
from flask import Flask, render_template
from filters import filters

app = Flask(__name__, template_folder='./templates')

for name, callback in filters.items():
    app.add_template_filter(callback, name)


@app.route('/', methods=['GET'])
def index():
    title = '《Python 之禅》'
    return render_template('index9.html', **locals())


@app.route('/login', methods=['GET'])
def login():
    title = '登录中心'
    # 此处可实现登录逻辑
    return render_template('login.html', **locals())


@app.route('/commodity', methods=['GET'])
def commodity():
    title = '商品列表'
    commodities = [
        {
            'id': 1,
            'name': '倚天剑',
            'price': 32.5
        },
        {
            'id': 2,
            'name': '屠龙刀',
            'price': 26
        },
        {
            'id': 3,
            'name': '葵花宝典',
            'price': 99
        },
        {
            'id': 4,
            'name': '吸星大法',
            'price': 18.8
        },
    ]
    return render_template('commodity.html', **locals())


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
