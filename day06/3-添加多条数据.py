import db
from model import Student


def run():
    students = [
        Student(name='汪伦', age=19, class_=3, description='滚出去', ),
        Student(name='上官丽丽', age=18, sex=False, class_=1, description='滚进来', ),
    ]
    db.session.add_all(students)
    db.session.commit()


if __name__ == '__main__':
    run()
