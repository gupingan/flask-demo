import json
from flask import Flask, request, make_response, Response, jsonify, redirect, url_for

app = Flask(__name__)


@app.route('/sms/<int:mobile>', methods=['GET', 'POST'])
def sms(mobile):
    return f'发送短信给 {mobile}'


@app.route('/info')
def info():
    url = url_for('sms', mobile='12345678')
    # return redirect('/sms/123456')
    return redirect(url)


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
