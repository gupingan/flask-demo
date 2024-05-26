from flask import Flask, request, current_app, g, session

app = Flask(__name__)

app.secret_key = 'my secret key'


@app.route('/', methods=['GET', 'POST'])
def index():
    print(session)
    print(request)
    print(current_app)
    print(app is current_app)
    print(app == current_app)
    """
    <SecureCookieSession {}>
    <Request 'http://127.0.0.1:9527/' [GET]>
    <Flask '3-上下文全局变量'>
    False
    True
    """
    return 'Hello Flask'


@app.route('/set_value/<int:value>', methods=['GET'])
def set_value(value):
    g.value = value
    return {'success': True, 'data': {'value': g.value}, 'msg': 'success'}


if __name__ == '__main__':
    with app.app_context():
        print(current_app)
    app.run('0.0.0.0', 9527, debug=True)
