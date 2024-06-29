import datetime
from db import *


class StudentCourse(db.Model):
    __tablename__ = 'tb_student_course2'

    id = db.Column(db.Integer, primary_key=True, comment='主键')
    sid = db.Column(db.Integer, db.ForeignKey('tb_nvm_student2.id'), comment='学生编号')
    cid = db.Column(db.Integer, db.ForeignKey('tb_nvm_course2.id'), comment='课程编号')
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')

    student = db.relationship('Student', uselist=False, backref=backref('to_relation', uselist=True, lazy='dynamic'))
    course = db.relationship('Course', uselist=False, backref=backref('to_relation', uselist=True, lazy='dynamic'))

    def to_dict(self):
        base = self.course.to_dict()
        base['sid'] = self.sid
        base['create_time'] = self.create_time.strftime('%Y-%m-%d %H:%M:%S')
        return base


class Student(db.Model):
    __tablename__ = 'tb_nvm_student2'

    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), index=True, comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    money = db.Column(db.Numeric(10, 2), default=0.0, comment="钱包")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'sex': self.sex,
            'money': float(self.money)
        }

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}>'


class Course(db.Model):
    __tablename__ = "tb_nvm_course2"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(255), unique=True, comment="课程")
    price = db.Column(db.Numeric(8, 2), comment="价格")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': float(self.price)
        }

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name}>"
