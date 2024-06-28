import db
from model import Student


def run():
    q4 = db.select(Student).where(db.not_(db.and_(Student.class_ == 1, Student.sex == 0)))
    students = db.session.execute(q4).scalars()
    for stu in students:
        print(stu.to_dict())
    students = db.session.query(Student).filter(db.not_(db.and_(Student.class_ == 1, Student.sex == 0))).all()
    for stu in students:
        print(stu.to_dict())


if __name__ == '__main__':
    run()
