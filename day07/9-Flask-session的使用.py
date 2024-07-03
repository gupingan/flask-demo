import json
from flask import Flask, request, session, render_template, redirect, url_for

app = Flask(__name__, template_folder='./')

# Flask 中的 session 基于 cookie 实现的，所以使用前必须设置 SECRET_KEY
app.config['SECRET_KEY'] = 'asdf1234'


@app.route('/set_session', methods=['GET', 'POST'])
def set_session():
    # Flask 中的 session 信息是保存在浏览器客户端的，因此不建议存储敏感信息
    # 浏览器调试终端可调用 atob 解析前半段得到原始数据
    session['username'] = '明儿'
    session['user_id'] = "101"
    return 'Hello Flask'


@app.route('/get_session', methods=['GET', 'POST'])
def get_session():
    username = session.get('username')
    user_id = session.get('user_id')
    print('username: ', username)
    print("user_id: ", user_id)
    return 'Hello Flask'


@app.route('/del_session', methods=['GET', 'POST'])
def del_session():
    session.pop('username')
    return 'Hello Flask'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == '12345678':
            session['username'] = username
            session['user_id'] = username
            return redirect(url_for('user'), 302)
        return redirect('/login', 302)
    return 'NOT FOUND'


@app.route('/user', methods=['GET', 'POST'])
def user():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'), 302)
    return f'用户中心 - {username}'


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
