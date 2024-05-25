import json
from flask import Flask, make_response, Response, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # 1. 接受请求
    # 2. 根据请求操作
    # 3. 响应数据
    # 响应 Html 文本
    # 元组 html, 状态码
    # return '<h1>Hello, Flask</h1>', 400
    # make_response
    # response = make_response('<h1>Hello, Flask</h1>', 201)
    # return response
    # Response
    return Response('<h1>Hello, Flask</h1>', 202)


@app.route('/json/api')
def json_api():
    data = {'name': '小明'}
    # 原生的写法
    # return json.dumps(data), 200, {'Content-Type': 'application/json'}
    # return Response(json.dumps(data), 200, {'Content-Type': 'application/json'})
    return jsonify(data), 201


@app.route('/img', methods=['GET'])
def img():
    with open('./avatar.jpg', 'rb') as fr:
        data = fr.read()

    return data, 201, {'Content-Type': 'image/jpeg'}


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
