import db
from model import Student


def run():
    q = db.select(Student).where(Student.id == 1)
    student = db.session.execute(q).scalar()
    print(student.to_dict())
    # q = db.delete(Student).where(Student.id == 1)
    # db.session.execute(q)
    db.session.delete(student)
    db.session.commit()
    q = db.select(Student).where(Student.id == 1)
    student = db.session.execute(q).scalar()
    print(student)


if __name__ == '__main__':
    run()
