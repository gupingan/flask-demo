import json
from flask import Flask, request, make_response, Response, jsonify, render_template, redirect, url_for

app = Flask(__name__, template_folder='./')


@app.route('/set_cookie', methods=['GET', 'POST'])
def set_cookie():
    """
    cookie 保存客户端浏览器中，cookie必须跟着响应对象返回
    :return:
    """
    response = make_response('set_cookie')
    # 基于响应对象提供的 set_cookie 方法，设置单个 cookie
    # response.set_cookie('变量名', '变量值', max_age='生命周期')
    # 如果没有设置 max_age，浏览器关闭时 cookie 将被销毁
    response.set_cookie('user_id', '100')
    # 如果设置了 max_age，按秒做时间单位，设置 cookie 的有效时间
    response.set_cookie('username', 'Ming', max_age=3600)
    response.set_cookie('number', '10086', max_age=3600)
    return response


@app.route('/get_cookie', methods=['GET', 'POST'])
def get_cookie():
    print('user_id:', request.cookies.get('user_id'))
    print('username:', request.cookies.get('username'))
    print('number:', request.cookies.get('number'))
    return 'Hello Flask'


@app.route('/del_cookie', methods=['GET', 'POST'])
def del_cookie():
    # cookie 保存在客户端，所以服务端无法删除
    # 要实现删除 cookie，只能告诉浏览器 cookie 过期了，让浏览器自动删除
    response = make_response('del_cookie')
    response.set_cookie('number', '', max_age=0)
    return response


@app.route('/login', methods=['GET', 'POST'])
def login():
    #     html = '''<!DOCTYPE html>
    # <html lang="en">
    # <head>
    #     <meta charset="UTF-8">
    #     <title>登录</title>
    # </head>
    # <body>
    # <form action="">
    #     账号：<label>
    #     <input type="text" name="username" , placeholder="请输入用户名">
    # </label><br>
    #     密码：<label>
    #     <input type="password" name="password" placeholder="输入密码">
    # </label><br>
    #     <input type="submit" value="登录">
    # </form>
    #
    # </body>
    # </html>'''
    #     return make_response(html)
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'root' and password == 'admin':
            # 基于 cookie 保存登录状态  重定向到用户中心
            response = redirect(url_for('user'), 302)
            # 设置 cookie
            response.set_cookie('username', username, max_age=7200)
            response.set_cookie('user_id', username, max_age=7200)
            return response
        return redirect(url_for('login'), 302)

    return Response('Not Found', 404)


@app.route('/user', methods=['GET', 'POST'])
def user():
    # 基于 cookie 的简单认证
    if not request.cookies.get('username'):
        return redirect(url_for('login'))
    return f'个人中心 - {request.cookies.get("username")}'


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
