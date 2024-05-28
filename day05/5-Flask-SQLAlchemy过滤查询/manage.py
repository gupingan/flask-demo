from pathlib import Path
from flask import Flask, jsonify, request
from config import Config
from models import db, Student, distinct, and_, or_, not_

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


@app.route('/students/filter', methods=['GET'])
def filter_student():
    """
    以下过滤查询操作，均含有不同版本 SQLAlchemy 的 API
    对应接口都是能够互相使用的（暂时可以，不考虑未来废弃的情况）
    :return:
    """
    # 去重复
    # /////////////////////////////////////////////////////////////////////////////////
    students = db.session.query(distinct(Student.age)).all()
    print(students)

    # 模糊查询
    # /////////////////////////////////////////////////////////////////////////////////
    # 使用`谷歌邮箱`的学生 method 1
    students = Student.query.filter(Student.email.contains('gmail.com')).all()
    print(students)
    # 使用`谷歌邮箱`的学生 method 2
    students = db.session.execute(db.select(Student).where(Student.email.like('%gmail.com'))).scalars().all()
    print(students)
    # 名字姓`王`的学生
    students = Student.query.filter(Student.name.startswith('王')).all()
    print(students)
    # 名字以`宇`结尾的学生
    students = Student.query.filter(Student.name.endswith('宇')).all()
    print(students)

    # 比较查询
    # /////////////////////////////////////////////////////////////////////////////////
    # 年龄超过 20 岁的学生
    students = Student.query.filter(Student.age > 20).all()
    print(students)
    students = db.session.execute(db.select(Student).where(Student.age > 20)).scalars().all()
    print(students)
    # 年龄超过 20 的男学生
    # students = db.session.execute(db.select(Student).where(Student.age > 20, Student.sex)).scalars().all()
    students = db.session.execute(db.select(Student).where(and_(Student.age > 20, Student.sex))).scalars().all()
    print(students)
    # 年龄超过 22 或者 年龄小于等于 20 的学生
    students = db.session.execute(db.select(Student).where(or_(Student.age > 22, Student.age <= 20))).scalars().all()
    print(students)
    # 钱包超过 4000 的女学生 或者 钱包超过 5000 的男学生
    students = db.session.execute(db.select(Student).where(
        or_(
            and_(Student.money > 4000, not Student.sex), and_(Student.sex, Student.money > 5000)
        )
    )).scalars().all()
    print(students)
    # 不姓 `王`、`李` 的所有学生
    # students = db.session.execute(db.select(Student).where(
    #     not_(
    #         or_(Student.name.startswith('王'), Student.name.startswith('李'))
    #     )
    # )).scalars().all()
    students = db.session.execute(db.select(Student).where(
        not_(Student.name.startswith('王')),
        not_(Student.name.startswith('李'))
    )).scalars().all()
    print(students)

    # 精确查询
    # /////////////////////////////////////////////////////////////////////////////////
    # 查询年龄为 22 的男学生
    students = db.session.execute(db.select(Student).where(Student.age == 22, Student.sex)).scalars().all()
    print(students)
    students = Student.query.filter_by(age=22, sex=True).all()
    print(students)

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
