import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    print(request, type(request))
    return 'Hello, Flask'


@app.route('/form1', methods=['POST'])
def form1():
    # 不包含文件
    print(request.form)
    print(request.form.get('form_name'))
    print(request.form.getlist('fav'))
    return form1.__name__


@app.route('/json1', methods=['POST'])
def json1():
    print(request.is_json)
    if request.is_json:
        print(request.json)
        print(request.json.get('name'))
    print(request.data)
    print(json.loads(request.data))
    return json1.__name__


@app.route('/file1', methods=['POST', 'PUT', 'PATCH'])
def file1():
    avatar = request.files.get('avatar')
    avatars = request.files.getlist('avatar')
    print(request.headers)
    print(avatar)
    print(avatar.mimetype)
    print(avatars)
    # print(avatar.stream.read())
    # avatar.save('./avatar.jpg')
    for a in avatars:
        print(a.mimetype)
        a.save(a.filename)
    return file1.__name__


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
