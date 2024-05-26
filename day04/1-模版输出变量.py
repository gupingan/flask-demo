import datetime
from flask import Flask, render_template, current_app, g, request

app = Flask(__name__, template_folder='./templates')


class User:
    desc = '用户类'

    def __str__(self):
        return '我是自定义的 User 类'


@app.route('/', methods=['GET'])
def index():
    # 基本数据类型
    title = '主页'
    number1 = 10086
    number2 = 3.14
    is_user = True
    # 容器类型
    bags = {'铅笔', '书包', '橡皮擦'}
    info = {
        'name': 'root',
        'gender': 'boy'
    }
    fans = ['小王', '老王', '金庸']
    fans_tuple = tuple(fans)
    # 复合数据类型
    fans_info = [
        {
            'name': '小王',
            'age': 18,
        },
        {
            'name': '老王',
            'age': 32,
        },
        {
            'name': '金庸',
            'age': 28,
        },
    ]
    book_list = [
        {
            'id': 10001,
            'name': '大主宰',
            'price': 26.6,
            'released': datetime.datetime.now()
        }
    ]
    # Flask 不分对象
    copy_app = current_app
    copy_app.config['VALUE_1'] = 'value 1'
    g.uname = 'root'
    # 自定义的对象
    user = User()
    return render_template('index1.html', **locals())


@app.route('/user1/<int:uid>')
def user1(uid):
    return f'{uid}'


@app.route('/user2')
def user2():
    uid = request.args.get('uid', '没有uid')
    return f'{uid}'


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
