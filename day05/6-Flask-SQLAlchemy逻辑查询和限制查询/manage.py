from pathlib import Path
from flask import Flask, jsonify, request
from config import Config
from models import db, Student, and_, or_, not_

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


@app.route('/students/data', methods=['GET'])
def students_data():
    print(Student.query.filter(Student.age > 16, Student.sex).all())
    print(Student.query.filter(and_(Student.age > 16, Student.sex)).all())
    print(Student.query.filter(or_(Student.age > 16, Student.sex)).all())
    print(Student.query.filter(not_(Student.age > 16)).all())
    print(Student.query.filter(not_(and_(Student.age > 16, Student.sex))).all())
    # 查询age是18 或者 money大于4000的所有学生
    print(Student.query.filter(or_(Student.age == 18, Student.money > 400)).all())
    # 查询id为 [1, 3, 5, 7, 9] 的学生列表
    ids = [1, 3, 5, 7, 9]
    print(Student.query.filter(Student.id.in_(ids)).all())
    for id_ in ids:
        print(Student.query.filter_by(id=id_).all())
    # 限制查询，年龄最大的3个学生
    print(Student.query.order_by(Student.age.desc()).limit(3).all())
    # 限制查询，年龄最小的第2至第3名
    print(Student.query.order_by(Student.age.asc()).offset(1).limit(2).all())
    return 'Data'


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run('0.0.0.0', 9527)
