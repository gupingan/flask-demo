from pathlib import Path
from flask import Flask, jsonify, request
from config import Config
from models import db, Student

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    title = Path(__file__).name
    return title


@app.route('/students', methods=['POST'])
def create_student():
    sex = request.form.get('sex')
    sex = int(sex) if sex.isdigit() else 0
    student = Student(
        name=request.form.get('name', '未知'),
        age=request.form.get('age', 0),
        sex=bool(sex),
        email=request.form.get('email', ''),
        money=request.form.get('money', 0),
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


@app.route('/students', methods=['DELETE'])
def delete_students():
    db.session.execute(db.delete(Student))
    db.session.commit()
    return jsonify({
        'success': True,
        'data': None,
        'msg': 'success'
    })


@app.route('/students', methods=['GET'])
def get_students():
    # 旧版本 2.x 获取全部数据
    # students = Student.query.all()
    # 新版本 3.1.x 获取全部数据
    students = db.session.execute(db.select(Student).where()).scalars()
    return jsonify({
        'success': True,
        'data': {
            'count': Student.query.count(),
            'students': [student.to_dict() for student in students]
        },
        'msg': 'success'
    })


@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    # 根据主键查询数据，不存在则为 None
    student = db.session.get(Student, student_id)
    if not student:
        return jsonify({
            'success': False,
            'data': None,
            'msg': 'student not found'
        })

    return jsonify({
        'success': True,
        'data': student.to_dict(),
        'msg': 'success'
    })


@app.route('/students/query', methods=['GET'])
def query_student():
    student = Student.query.first()
    if student:
        print(student.to_dict())
    student = Student.query.filter(Student.sex == False).first()
    if student:
        print(student.to_dict())
    students = Student.query.filter_by(age=22)
    print(students)
    students = Student.query.filter(Student.age == 22).all()
    if students:
        print(students[-1])

    return jsonify({
        'success': True,
        'data': None,
        'msg': 'success'
    }), 201


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run('0.0.0.0', 9527)
