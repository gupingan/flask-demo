from models import *

# 删除表格
# ///////////////////////////////////////////////
db.Base.metadata.drop_all(db.engine)

# 创建表格
# ///////////////////////////////////////////////
db.Base.metadata.create_all(db.engine)

# 添加一条记录
# ///////////////////////////////////////////////
added_student = Student(
    name='张三丰',
    sex=True,
    age=25,
    class_name='x-101',
    description='太极门老大'
)
db.session.add(added_student)
db.session.commit()

# 添加多条记录
# ///////////////////////////////////////////////
added_students = [
    Student(name='萧炎', sex=True, age=23, class_name='x-102', description='斗破苍穹男主'),
    Student(name='柳神', sex=False, age=23, class_name='x-102', description='完美世界一代绝世仙王'),
    Student(name='张无忌', sex=True, age=32, class_name='x-101', description='倚天屠龙记男主'),
]
db.session.add_all(added_students)
db.session.commit()

# 获取模型对应表的所有数据
# ///////////////////////////////////////////////
# 1.4 版本
# all_students = db.session.query(Student).all()
# print(all_students)
# 2.0 版本
all_students = db.session.execute(db.select(Student).where()).scalars().all()
# for student in all_students:
#     print(f"{student.name}, {student.age}, {student.description}")
print(list(all_students))
# stmt = db.select(Student).where()
# all_students = db.session.scalars(stmt).all()
# for student in all_students:
#     print(f"{student.name}, {student.age}, {student.description}")
# print(list(all_students))

# 更新 1 条记录
# ///////////////////////////////////////////////
try:
    student = db.session.execute(db.select(Student).where(Student.name == '张三丰')).scalar_one()
    print(student)
    student.name = '张四丰'
    db.session.commit()
    print(student)
except db.exc.NoResultFound:
    print('角色不存在')

# 更新多条记录(也可只更新一条记录)
# ///////////////////////////////////////////////
db.session.execute(db.update(Student).where(Student.class_name == 'x-102').values(age=Student.age+1))
db.session.commit()

# 删除 1 条数据
# ///////////////////////////////////////////////
added_student = Student(
    name='冒牌张三丰',
    sex=True,
    age=28,
    class_name='x-101',
    description='太极门老大 - 伪'
)
db.session.add(added_student)
db.session.commit()
try:
    student = db.session.execute(db.select(Student).where(Student.name == '冒牌张三丰')).scalar_one()
    print(student.name, student.id, student.description)
except db.exc.NoResultFound:
    print('未找到此人')
else:
    # db.session.delete(student)
    # db.session.commit()
    db.session.execute(db.delete(Student).where(Student.name == '冒牌张三丰'))
    db.session.commit()

# 删除多条数据
# ///////////////////////////////////////////////
added_students = [
    Student(
        name='冒牌张三丰',
        sex=True,
        age=28,
        class_name='x-101',
        description='太极门老大 - 伪'
    ),
    Student(
        name='冒牌张三丰',
        sex=True,
        age=28,
        class_name='x-101',
        description='太极门老大 - 伪'
    ),
    Student(
        name='冒牌张三丰',
        sex=True,
        age=28,
        class_name='x-101',
        description='太极门老大 - 伪'
    )
]
db.session.add_all(added_students)
db.session.commit()
db.session.execute(db.delete(Student).where(Student.name.like('%冒牌张三丰%')))
db.session.commit()
# # db.session.execute(db.delete(Student).where(Student.name == '冒牌张三丰'))
# # db.session.commit()

# 排序
# ///////////////////////////////////////////////
students1 = db.session.execute(db.select(Student).order_by(Student.age)).scalars().all()
print('单字段升序', students1)
students2 = db.session.execute(db.select(Student).order_by(Student.age.desc())).scalars().all()
print('单字段降序', students2)
students3 = db.session.execute(db.select(Student).order_by(Student.age.desc(), Student.id.desc())).scalars().all()
print('多字段排序', students3)


# 原生 SQL 语句
# ///////////////////////////////////////////////
cursor = db.session.execute(db.text('select * from `tb_student1`'))
print(cursor.fetchmany())
print(cursor.fetchone())
db.session.execute(
    db.text('insert into `tb_student1`(name, class, age, sex, description) values(:name, :class_name, '
            ':age, :sex, :description)'),
    params=dict(name='小红', class_name='x-103', age=19, sex=False, description='临时添加')
)
db.session.commit()
