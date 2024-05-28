from pathlib import Path
from flask import Flask
from config import Config
from models import db, Course

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    title = Path(__file__).name
    course = Course(name='《顶级 Kali Linux 技术简明教程》', price=32.5)
    db.session.add(course)
    db.session.commit()
    return title


if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()
        db.create_all()
    app.run('0.0.0.0', 9527)
