import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/header', methods=['GET', 'POST'])
def index():
    # 获取请求头所有信息
    print(request.headers)
    print(type(request.headers))
    # 获取单个请求头信息
    print(request.host)
    print(request.user_agent)  # 原始属性名转成小写下划线命名法格式
    print(request.headers.get('User-Agent'))
    print(request.content_type)
    print(request.path)
    print(request.url)
    print(request.url_root)
    print(request.root_url)
    print(request.base_url)
    print(request.method)
    print(request.remote_addr)
    print(request.server)
    print(request.environ)
    # 获取自定义的请求头
    print(request.headers.get('Company'))
    return 'Hello, Flask'


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
