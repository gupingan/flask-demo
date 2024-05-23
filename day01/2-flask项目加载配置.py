from flask import Flask

app = Flask(__name__)

# 1. 字典或者对象
app.config['DEBUG'] = True
# app.config.update({'DEBUG': True})
# app.config.update(
#     DEBUG=True,
#     SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
# )

# class Config:
#     DEBUG = True
# app.config.from_object(Config)
# app.config.from_object(Config())
# app.config.from_object('config')

# import config
# app.config.from_object(config)


# 2. 文件导入配置
# app.config.from_pyfile('./config.py')

# import json
# app.config.from_file('config.json', load=json.load)

# python 3.11 支持 toml 配置
# import tomllib
# others poetry add toml  or  pip install toml
# import toml
# app.config.from_file('config.toml', load=toml.load)


# 3. 环境变量配置
# before(windows): $env:FLASK_DEBUG = 0
# app.config.from_prefixed_env()

# before(windows): $env:FLASK_SETTINGS = "D:\study\python-flask\flask-demo\day01\settings.cfg"
# app.config.from_envvar('FLASK_SETTINGS')


@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/welcome')
def welcome():
    return '<h1>你好，Flask</h1>'


if __name__ == '__main__':
    app.run('0.0.0.0', 9527)
