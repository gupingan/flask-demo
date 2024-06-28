from db import *


class Student(db.Model):
    __tablename__ = 'tb_1v1_student'

    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), index=True, comment="姓名")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}>'


class StudentInfo(db.Model):
    __tablename__ = 'tb_1v1_student_info'

    id = db.Column(db.Integer, primary_key=True, comment='主键')
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, comment="性别")
    email = db.Column(db.String(128), unique=True, comment="邮箱地址")
    money = db.Column(db.Numeric(10, 2), default=0.0, comment="钱包")

    stu_id = db.Column(db.Integer, db.ForeignKey('tb_1v1_student.id'), unique=True, comment='外键')
    student = db.relationship('Student', uselist=False, backref=backref('info', uselist=False))

    def to_dict(self):
        info = {
            'id': self.id,
            'stu_id': self.student.id,
            'name': self.student.name,
            'age': self.age,
            'sex': self.sex,
            'email': self.email,
            'money': float(self.money)
        }
        return info

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.student.name}>'
