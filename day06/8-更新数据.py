import db
from model import Student


def run():
    q = db.select(Student).where(Student.id == 1)
    student = db.session.execute(q).scalar()
    print(student.to_dict())
    student.name = '张晓明'
    db.session.commit()
    print(student.to_dict())


if __name__ == '__main__':
    run()
