from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    print(request, type(request))
    return 'Hello, Flask'


users = [
    {
        'id': 2,
        'name': '王城'
    },
    {
        'id': 1,
        'name': '龙八天'
    },
]


@app.route('/user')
def get_user():
    # http://127.0.0.1:9527/user?uid=1&fav=edit
    print(request.query_string)  # b'uid=1&fav=edit'
    from urllib.parse import parse_qs
    parse_result = parse_qs(request.query_string.decode())
    print(parse_result)  # {'uid': ['1'], 'fav': ['edit']}
    print(request.args)  # ImmutableMultiDict([('uid', '1'), ('fav', 'edit')])
    uid = request.args.get('uid')
    if uid:
        f_user = next((user for user in users if str(user['id']) == uid), None)
        if f_user:
            return f'查询到了 {f_user}'
    return '暂未查询到'


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
