import db
from model import Student


def run():
    q3 = db.select(Student).where(Student.class_ == 3)
    students = db.session.execute(q3).scalars()
    for stu in students:
        print(stu.to_dict())
    students = db.session.query(Student).filter_by(class_=3).all()  # 不支持 大于小于等 范围
    print(students)
    students = db.session.query(Student).filter(Student.class_ == 3).all()
    print(students)


if __name__ == '__main__':
    run()
