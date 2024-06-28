import db
from model import Student


def run():
    students = db.session.query(Student).filter(Student.id.in_([1, 2])).all()
    for stu in students:
        print(stu.to_dict())
    q5 = db.select(Student).where(Student.id.in_([1, 2]))
    students = db.session.execute(q5).scalars()
    for stu in students:
        print(stu.to_dict())


if __name__ == '__main__':
    run()
