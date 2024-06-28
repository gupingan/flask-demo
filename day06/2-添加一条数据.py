import db
from model import Student


def run():
    student = Student(
        id=1,
        name='王小明',
        age=18,
        class_=3,
        description='滚出去',
    )
    db.session.add(student)
    db.session.commit()
    print(student.to_dict())


if __name__ == '__main__':
    run()
