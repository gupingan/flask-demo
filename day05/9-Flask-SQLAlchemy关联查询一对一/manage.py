from flask import Flask, request, jsonify
from pathlib import Path
from config import Config
from models import db, Student, StudentInfo

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    title = Path(__file__).name
    return title


@app.route('/students', methods=['POST'])
def create_student():
    # 添加主模型的同时添加外键模型
    # 也可以添加外键模型的同时添加主模型
    # 已经有了主模型，可以赋值新的外键模型
    sex = request.form.get('sex')
    sex = int(sex) if sex.isdigit() else 0
    student = Student(
        name=request.form.get('name', '未知'),
        info=StudentInfo(
            age=request.form.get('age', 0),
            sex=bool(sex),
            email=request.form.get('email', ''),
            money=request.form.get('money', 0),
        )
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
    db.session.execute(db.delete(StudentInfo))
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
    # students = db.session.query(Student).all()
    # print(students)
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


@app.route('/query', methods=['GET'])
def data():
    student = Student.query.filter(Student.id == 1).first()
    print(student.info)
    print(student.info.student)
    info = StudentInfo.query.filter(Student.name == '王毅').first()
    print(info.student)
    print(info.student.info)
    info = StudentInfo.query.filter(StudentInfo.stu_id == student.id).first()
    print(info.student)
    print(info.student.info)
    return 'Data'


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run('0.0.0.0', 9527)
