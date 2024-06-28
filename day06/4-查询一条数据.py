import db
from model import Student


def run():
    student = db.session.query(Student).get(1)  # 单个主键 联合主键则使用(1,2) 或者 {'id': 1, 'class_id': 2}
    print(student.to_dict())
    q1 = db.select(Student)
    student = db.session.execute(q1).scalar()
    print(student.to_dict())
    q1 = db.select(Student).where(Student.id == 1)
    student = db.session.execute(q1).scalar()
    print(student.to_dict())
    student = db.session.query(Student).filter_by(id=1).first()
    print(student.to_dict())
    print(student.__dict__)


if __name__ == '__main__':
    run()
