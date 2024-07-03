from flask import Flask
from users import users_app

app = Flask(__name__)

app.register_blueprint(users_app)


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
