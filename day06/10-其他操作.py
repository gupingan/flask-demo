import db
from model import Student


def run():
    # 限制结果数量
    # q = db.select(Student).where(Student.id.in_([1, 2, 3])).limit(2)
    # students = db.session.execute(q).scalars()
    # for stu in students:
    #     print(stu.to_dict())
    # students = db.session.query(Student).filter(Student.id.in_([1, 2, 3])).limit(2).all()
    # for stu in students:
    #     print(stu.to_dict())
    # 排序
    # q = db.select(Student).order_by(Student.class_.asc())
    # students = db.session.execute(q).scalars()
    # for stu in students:
    #     print(stu.to_dict())
    # q = db.select(Student).order_by(Student.id.desc())
    # students = db.session.execute(q).scalars()
    # for stu in students:
    #     print(stu.to_dict())
    # 事务操作
    try:
        db.session.begin()
    except Exception as e:
        print(e)
        db.session.rollback()
    else:
        db.session.commit()


if __name__ == '__main__':
    run()
