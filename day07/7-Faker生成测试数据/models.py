import datetime
from db import *


class Student(db.Model):
    __tablename__ = 'tb_faker_student'

    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), index=True, comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), default='', comment='联系邮箱')
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='联系邮箱')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'sex': self.sex,
            'email': self.email,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
        }

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}>'
