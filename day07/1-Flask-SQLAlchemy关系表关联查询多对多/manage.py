from flask import Flask, request, jsonify
from pathlib import Path
from config import Config
from models import db, Student, Course, func

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)


# db.Table的缺陷: 无法通过主模型直接操作db.Table中的外键之外的其他字段，例如：无法读取购买课程的时间

@app.route('/', methods=['GET'])
def index():
    title = Path(__file__).name
    return title


@app.route('/students', methods=['POST'])
def create_student():
    student = Student(
        name=request.form.get('name', '未知'),
        age=request.form.get('age', 18),
        sex=bool(request.form.get('sex') == '1'),
        money=request.form.get('money', 0)
    )
    if request.form.get('id', None) is not None:
        student.id = request.form['id']

    db.session.add(student)
    db.session.commit()
    return jsonify({
        'success': True,
        'data': student.to_dict(),
        'msg': 'success'
    }), 201


@app.route('/courses', methods=['POST'])
def create_course():
    course = Course(
        name=request.form.get('name', '未知'),
        price=request.form.get('price', 0)
    )
    db.session.add(course)
    db.session.commit()
    return jsonify({
        'success': False,
        'data': course.to_dict(),
        'msg': 'success'
    })


@app.route('/drop', methods=['DELETE'])
def drop_tables():
    with app.app_context():
        db.drop_all()
        db.create_all()
    return jsonify({
        'success': True,
        'data': None,
        'msg': 'success'
    })


@app.route('/buy', methods=['POST'])
def buy_course():
    student = Student.query.get(request.form.get('sid', -1))
    if not student:
        return jsonify({
            'success': False,
            'data': None,
            'msg': '学生不存在'
        })

    course_ids = request.form.getlist('course_ids', type=int)
    q = db.select(func.sum(Course.price)).where(Course.id.in_(course_ids))
    price = db.session.execute(q).scalar()
    if price is None or price > student.money:
        return jsonify({
            'success': False,
            'data': None,
            'msg': '钱不够'
        })

    student.money -= price

    q = db.select(Course).where(Course.id.in_(course_ids))
    courses = db.session.execute(q).scalars()
    student.courses.extend(courses)

    db.session.commit()

    return jsonify({
        'success': True,
        'data': None,
        'msg': '购买成功'
    })


@app.route('/query', methods=['GET'])
def data():
    sid = request.args.get('sid', type=int)
    if not sid:
        jsonify({
            'success': False,
            'data': None,
            'msg': '学生编号不合法'
        })

    student = Student.query.get(sid)
    if not student:
        jsonify({
            'success': False,
            'data': None,
            'msg': '学生不存在'
        })

    base = student.to_dict()
    base['courses'] = [course.to_dict() for course in student.courses.all()]

    return jsonify({
        'success': True,
        'data': base,
        'msg': '查询成功'
    })


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run('0.0.0.0', 9527)
