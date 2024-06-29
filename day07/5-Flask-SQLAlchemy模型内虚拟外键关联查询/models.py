import datetime
from db import *


class StudentCourse(db.Model):
    __tablename__ = 'tb_vk_student_course'

    id = db.Column(db.Integer, primary_key=True, comment='主键')
    sid = db.Column(db.Integer, index=True, comment='学生编号')
    cid = db.Column(db.Integer, index=True, comment='课程编号')
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    # 关联属性[比原来设置物理外键，多出2个属性设置：primaryjoin 与 foreign_keys]
    student = db.relationship(
        'Student', uselist=False,
        backref=backref('to_relation', uselist=True, lazy='dynamic'),
        primaryjoin='Student.id==StudentCourse.sid',
        foreign_keys='StudentCourse.sid'
    )
    course = db.relationship(
        'Course', uselist=False,
        backref=backref('to_relation', uselist=True, lazy='dynamic'),
        primaryjoin='Course.id==StudentCourse.cid',
        foreign_keys='StudentCourse.cid'
    )

    def to_dict(self):
        return {
            'sid': self.sid,
            'cid': self.cid,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
        }


class Student(db.Model):
    __tablename__ = 'tb_vk_nvm_student'

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
    __tablename__ = "tb_vk_nvm_course"
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
