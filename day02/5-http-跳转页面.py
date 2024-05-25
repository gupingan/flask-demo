import json
from flask import Flask, request, make_response, Response, jsonify, redirect, url_for
from flask.globals import _cv_app
from werkzeug.routing.map import MapAdapter

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.args.get('token'):
        return '个人中心'
    # 跳转到登录视图
    # return redirect('/login')
    # print(app.url_map)
    return redirect(url_for('login'))


@app.route('/login', methods=['GET'])
def login():
    return '登录视图'


@app.route('/jump')
def jump():
    """
    301: 永久重定向，页面已经没有了，站点没有了，永久转移了。[域名映射-->域名解析]
    302：临时重定向，一般验证失败、访问需要权限的页面进行登录跳转时，都是属于临时跳转。
    """
    # return Response('', 302, {'Location': 'https://www.qq.com'})
    return redirect('https://www.qq.com', 302)


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
