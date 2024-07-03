# 1.构造蓝图对象
from flask import Blueprint

# 实例化蓝图，传入蓝图应用名称、相对引用名称，蓝图应用路由前缀
users_app = Blueprint('users', __name__, url_prefix='/users')


# 2.构造路由函数
def login():
    return '登录'


# 3.添加路由视图
# 创建一个匿名函数，存储到蓝图应用的 deferred_functions 列表中。该函数参数是蓝图状态对象，调用该匿名函数将路由添加到app应用中
users_app.add_url_rule('/login', view_func=login)

# 4.app注册蓝图对象
from flask import Flask

# 实例化app对象
app = Flask(__name__)

# 注册蓝图：调用被添加的蓝图应用的 register 方法
# 会根据当前环境构建蓝图状态对象，然后便利该蓝图应用中的 deferred_functions 列表
# 不断的调用蓝图状态对象的add_url_rule方法，从而完成路由视图、蓝图应用相关参数的注册
app.register_blueprint(users_app)

if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
