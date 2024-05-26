from pathlib import Path
from flask import Flask, render_template, request
from flask_wtf import CSRFProtect, csrf


app = Flask(__name__)

# 设置 CSRF 时，务必设置 SECRET_KEY
app.secret_key = 'my secret key'

csrf_token = CSRFProtect()
csrf_token.init_app(app)


@app.route("/")
def user():
    """
    如果出现服务器拒绝连接
    记得修改 index10.html 中表单的 action 指向
    因为可能主机地址和端口不同
    :return:
    """
    title = Path(__file__).name
    html = render_template("index10.html", **locals())
    return html


# @app.route("/transfer", methods=["POST"])
# def transfer_safe():
#     """
#     这是安全的转账模拟
#     :return:
#     """
#     print(request.form)
#     return "转账成功！"


@app.route("/transfer", methods=["POST"])
@csrf_token.exempt  # 排除该视图函数，也就是不验证 csrf_token
def transfer_unsafe():
    """
    这是不安全的转账模拟
    :return:
    """
    print(request.form)
    return "转账成功！"


@app.errorhandler(csrf.CSRFError)
def handle_csrf_error(e):
    """
    自定义 CSRF 错误时返回的响应
    :param e:
    :return:
    """
    print(e)
    return '一看你就没有 CSRF 吧！来人，抬走，略略略~'


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
