from flask import Flask, Response, request, abort, jsonify

app = Flask(__name__)


@app.teardown_request
def teardown_request(exc: Exception):
    """
    当请求从栈中被弹出时，会执行（响应给客户端之后执行）
    如果有异常，则 exe 为被捕捉到的异常（视图函数和 after_request 均不再执行）
    如果没有，则 exe 为 None，视图函数和 after_request 会正常执行
    不能返回
    :param exc:
    :return:
    """
    print('teardown_request', exc)


"""
abort:
    未调用abort时：
        --------view function---------
        teardown_request None
    调用abort时：
        --------view function---------
        403
        teardown_request None
抛出异常：
    未抛出时：
        --------view function---------
        teardown_request None
    抛出时：
        --------view function---------
        error_custom_exception
        teardown_request None
"""


class CustomException(Exception):
    description = '自定义异常'


@app.route('/', methods=['GET', 'POST'])
def index():
    print('view function'.center(30, '-'))
    password = request.args.get('password')
    if password != 'admin':
        # abort(403, description='禁止访问')
        raise CustomException

    return {'code': 200, 'data': {'password': password}, 'msg': 'success'}


@app.errorhandler(403)
def error_403(exc):
    print('error_403')
    return {'code': 403, 'data': None, 'msg': exc.description}


@app.errorhandler(CustomException)
def error_custom_exception(exc):
    print('error_custom_exception')
    return {'code': 500, 'data': None, 'msg': exc.description}


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
