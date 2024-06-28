import db
from model import Student


def run():
    q2 = db.select(Student)
    students = db.session.execute(q2).scalars()
    for stu in students:
        print(stu.to_dict())


if __name__ == '__main__':
    run()
