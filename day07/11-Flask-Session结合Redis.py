from flask import Flask, request, session, render_template, redirect, url_for
from flask_redis import FlaskRedis
from flask_session import Session as SessionStore

app = Flask(__name__, template_folder='./')

session_redis = FlaskRedis(config_prefix='REDIS_SESSION')
user_redis = FlaskRedis(config_prefix='REDIS_USER')
order_redis = FlaskRedis(config_prefix='REDIS_ORDER')
session_store = SessionStore()

app.config['SECRET_KEY'] = 'my-secret-key'
app.config['REDIS_SESSION_URL'] = 'redis://:0908@127.0.0.1:6379/0'
app.config['REDIS_USER_URL'] = 'redis://:0908@127.0.0.1:6379/1'
app.config['REDIS_ORDER_URL'] = 'redis://:0908@127.0.0.1:6379/2'
app.config.update({
    # 把session保存到redis中
    "SESSION_TYPE": "redis",  # session类型为sqlalchemy, redis 或 mongodb
    "SESSION_PERMANENT": True,  # 如果设置为True，则关闭浏览器session就失效
    "SESSION_USE_SIGNER": True,  # 是否对发送到浏览器上session的cookie值进行添加签名，防止串改。
    "SESSION_KEY_PREFIX": "session:",  # session数据表中sessionID的前缀，默认就是 session:
    # session保存数据到redis时启用的链接对象
    "SESSION_REDIS": session_redis,  # 用于连接redis的配置
})

session_redis.init_app(app)
user_redis.init_app(app)
order_redis.init_app(app)

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
