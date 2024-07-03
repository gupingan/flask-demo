from flask import Flask, request, session, render_template, redirect, url_for
from flask_session import Session as SessionStore
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='./')
db = SQLAlchemy()
session_store = SessionStore()

# 必须设置 SECRET_KEY
app.config['SECRET_KEY'] = 'asdf1234'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:0908@localhost:3306/db_flask_demo_school?charset=utf8mb4'
# 以下为 Flask-Session 的配置项
app.config.update({
    "SESSION_TYPE": "sqlalchemy",  # session类型为sqlalchemy
    "SESSION_SQLALCHEMY": db,  # SQLAlchemy的数据库连接对象
    "SESSION_SQLALCHEMY_TABLE": 'tb_sessions',  # session要保存的表名称
    "SESSION_PERMANENT": True,  # 如果设置为True，则关闭浏览器session就失效
    "SESSION_USE_SIGNER": True,  # 是否对发送到浏览器上session的cookie值进行添加签名，防止串改。
    "SESSION_KEY_PREFIX": "session:"  # session数据表中sessionID的前缀，默认就是 session:
})

db.init_app(app)
# 注册 session_store 之前，务必先注册 SqlAlchemy 对象
session_store.init_app(app)


@app.route('/set_session', methods=['GET', 'POST'])
def set_session():
    session['username'] = '明儿'
    session['user_id'] = "101"
    return 'Hello Flask'


@app.route('/get_session', methods=['GET', 'POST'])
def get_session():
    username = session.get('username')
    user_id = session.get('user_id')
    print('username: ', username)
    print("user_id: ", user_id)
    return f'用户ID：{user_id} 用户名：{username}'


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
