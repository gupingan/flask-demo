from flask import Flask, request, jsonify
from pathlib import Path
from config import Config
from models import db, Student, StudentAddress

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    title = Path(__file__).name
    return title


@app.route('/students', methods=['POST'])
def create_student():
    student = Student(name=request.form.get('name', '未知'), )
    if request.form.get('id', None) is not None:
        student.id = request.form['id']

    db.session.add(student)
    db.session.commit()
    return jsonify({
        'success': True,
        'data': student.to_dict(),
        'msg': 'success'
    }), 201


@app.route('/address', methods=['POST'])
def create_address():
    stu_id = request.args.get('id')
    student = Student.query.get(stu_id)
    if not student:
        return jsonify({
            'success': False,
            'data': None,
            'msg': 'student not found'
        })

    address = StudentAddress(
        name=request.form.get('name', '未知'),
        province=request.form.get('province', '未知省'),
        city=request.form.get('city', '未知市'),
        area=request.form.get('area', '未知区'),
        address=request.form.get('address', ''),
        mobile=request.form.get('mobile', '未知手机号码'),
    )

    student.addresses.append(address)
    db.session.commit()
    return jsonify({
        'success': False,
        'data': address.to_dict(),
        'msg': 'success'
    })


@app.route('/students', methods=['DELETE'])
def delete_students():
    db.session.execute(db.delete(StudentAddress))
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
    print(student)
    print(student.addresses)
    # subquery
    student = db.session.query(Student).get(1)
    print(student)
    print(student.addresses)
    # dynamic
    student = Student.query.get(2)
    print(student)
    print(student.addresses[0])
    # select
    student = Student.query.get(2)
    print(student)
    print(student.addresses[0])
    return 'Data'


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run('0.0.0.0', 9527)
