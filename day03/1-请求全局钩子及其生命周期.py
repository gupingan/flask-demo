from flask import Flask, Response

app = Flask(__name__)


# before_first_request 在 Flask 2.3.0 及其以后已被移除，通过工厂函数创建 app 时，提前部署好
# 比如：数据库连接、日志配置、延后引入的全局配置等等

@app.before_request
def before_request():
    """
    在接收到客户端请求后 到 视图函数执行前之间执行
    一般用于 【权限验证、身份认证、权限判断等等】
     - tip: 如果具备返回值，将不再执行视图函数
    :return:
    """
    print('before request')


@app.after_request
def after_reqeust(response: Response):
    """
    在视图函数执行完毕后 到 返回给客户端响应前之间执行
    一般用于 【返回格式加工、日志记录等等】
    该被装饰的函数必须填写形参 response
    :param response:
    :return:
    """
    print('after request', response.data)
    response.headers['Company'] = 'mima.com'
    return response


@app.teardown_request
def teardown_request(exe: Exception):
    """
    当请求从栈中被弹出时，会执行（响应给客户端之后执行）
    如果有异常，则 exe 为被捕捉到的异常（视图函数和 after_request 均不再执行）
    如果没有，则 exe 为 None，视图函数和 after_request 会正常执行
    不能返回
    :param exe:
    :return:
    """
    print('teardown_request', exe)


"""
请求响应正常时：
    before request
    --------view function---------
    after request b'Hello Flask'
    teardown_request None
视图函数报错时：
    before request
    teardown_request division by zero
"""


@app.route('/', methods=['GET', 'POST'])
def index():
    print('view function'.center(30, '-'))
    return 'Hello Flask'


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
