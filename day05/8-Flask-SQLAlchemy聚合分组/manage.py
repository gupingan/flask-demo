from pathlib import Path
from flask import Flask, jsonify, request
from config import Config
from models import db, Student, and_, or_, not_, func, text

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
    # 聚合
    ret = db.session.query(func.count(Student.id)).filter(not_(Student.sex)).first()[0]
    print(ret)
    ret = db.session.query(func.sum(Student.money)).first()[0]
    print(ret)
    ret = db.session.query(func.avg(Student.money)).first()[0]
    print(ret)
    # 分组
    ret = db.session.query(Student.age, func.avg(Student.money)).group_by(Student.age).all()
    print(ret)
    ret = db.session.query(Student.age, Student.sex, func.avg(Student.money)).group_by(Student.age, Student.sex).all()
    print(ret)
    # 分组过滤
    ret = db.session.query(Student.sex, func.max(Student.money)).group_by(Student.sex).all()
    print(ret)
    subquery = func.max(Student.money)
    ret = db.session.query(Student.sex, subquery).group_by(Student.sex).having(subquery < 7000).all()
    print(ret)
    # 原生 SQL 语句
    ret = db.session.execute(text('show databases')).all()
    print(ret)
    ret = db.session.execute(text('select * from db_flask_demo_school.tb_student2')).all()
    print(ret)
    ret = db.session.execute(
        text("select sex,max(money),group_concat(id) from db_flask_demo_school.tb_student2 group by sex")).fetchall()
    print(ret)
    return 'Data'


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run('0.0.0.0', 9527)
