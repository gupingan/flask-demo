from flask import url_for, render_template


def login():
    print(url_for('users.register'))
    return '登录'


def register():
    return '注册'


def demo():
    return render_template('demo.html')
