from pathlib import Path
from flask import Flask, jsonify, request, render_template
from config import Config
from models import db, Student

app = Flask(__name__, template_folder='./templates')
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
    # 不采取数据分页时，大量数据时会导致服务器运存膨胀，这是非常不妥的
    # 创建分页器对象
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('size', 3, type=int)
    pagination = Student.query.paginate(page=page, per_page=per_page, max_per_page=20)
    print('当前页对象', pagination)
    print('总数据量', pagination.total)
    print('当前页数据列表', pagination.items)
    print('总页码', pagination.pages)
    print()
    print('是否有上一页', pagination.has_prev)
    print('上一页页码', pagination.prev_num)
    print('上一页对象', pagination.prev())
    print('上一页对象的数据列表', pagination.prev().items)
    print()
    print('是否有下一页', pagination.has_next)
    print('下一页页码', pagination.next_num)
    print('下一页对象', pagination.next())
    print('下一页对象的数据列表', pagination.next().items)

    # """前后端分离"""
    data = {
        "page": pagination.page,  # 当前页码
        "pages": pagination.pages,  # 总页码
        "has_prev": pagination.has_prev,  # 是否有上一页
        "prev_num": pagination.prev_num,  # 上一页页码
        "has_next": pagination.has_next,  # 是否有下一页
        "next_num": pagination.next_num,  # 下一页页码
        "items": [{
            "id": item.id,
            "name": item.name,
            "age": item.age,
            "sex": item.sex,
            "money": item.money,
        } for item in pagination.items]
    }

    return render_template('list.html', **locals())


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run('0.0.0.0', 9527)
