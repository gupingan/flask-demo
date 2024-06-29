from flask import Flask, request, jsonify
from pathlib import Path
from config import Config
from models import db, Student, StudentAddress
from migrate import migrate

app = Flask(__name__)
# 加载配置
app.config.from_object(Config)
# 注册 SqlAlchemy 组件
db.init_app(app)
# 注册数据库迁移组件，绑定 app 和 db
migrate.init_app(app, db)


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
    app.run('0.0.0.0', 9527)


"""
1.切换当项目文件夹中，初始化 迁移文件
    > flask --app=manage:app db init
    Creating directory ...
    Generating ...
    Please edit configuration/connection/logging settings in ...

2.创建迁移版本
    - 自动创建迁移版本文件中有两个函数，用于进行数据迁移同步到数据库操作的。
      - upgrade()：把迁移中的改动代码同步到数据库中。
      - downgrade()：则将改动代码从数据库中进行还原。
    - 自动创建的迁移脚本会根据模型定义和数据库当前状态的差异，生成upgrade()和downgrade()函数的内容。
    - 生成的迁移文件不一定完全正确，有可能代码中存在细节遗漏导致报错，需要开发者进行检查，特别在多对多的时候
        迁移信息中尽量不要使用中文
    
    > flask --app=manage:app db migrate -m 'initial migration'
    INFO  [alembic.runtime.migration] Context impl MySQLImpl.
    INFO  [alembic.runtime.migration] ...
    Generating ...  done

3.升级版本
    > flask --app=manage:app db upgrade
    INFO  [alembic.runtime.migration] Context impl MySQLImpl.
    INFO  [alembic.runtime.migration] ...

4.降级版本
    > flask --app=manage:app db downgrade
    INFO  [alembic.runtime.migration] Context impl MySQLImpl.
    INFO  [alembic.runtime.migration] ...

版本库历史管理
    > flask --app=manage:app db history
    <base> -> 17406c2735a3 (head), initial migration

回滚到指定版本
    flask --app=manage:app db downgrade  # 默认返回上一个版本
    flask --app=manage:app db downgrade 版本号  # 回滚到指定版本号对应的版本
    flask --app=manage:app db upgrade  # 默认升级到最近的下一版本
    flask --app=manage:app db upgrade 版本号  # 升级到指定版本号对应的版本

步骤总结：
    新项目：init -> migrate -> upgrade -> [downgrade]
    原始项目：migrate -> upgrade[downgrade]

技巧：
    flask --app=manage:app 每次都需要指定 Flask 应用，可以将其设置为当前窗口的临时环境变量
    生产环境下，FLASK_APP是必须指定好的
    > export FLASK_APP=manage.py
"""