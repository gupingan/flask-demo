from db import *

table_student_course = db.Table(
    'tb_student_course',
    db.Column('id', db.Integer, primary_key=True, comment='主键'),
    db.Column('sid', db.Integer, db.ForeignKey('tb_nvm_student.id'), comment='学生编号'),
    db.Column('cid', db.Integer, db.ForeignKey('tb_nvm_course.id'), comment='可成编号'),
)


class Student(db.Model):
    __tablename__ = 'tb_nvm_student'

    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), index=True, comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    money = db.Column(db.Numeric(10, 2), default=0.0, comment="钱包")

    courses = db.relationship(
        'Course', uselist=True, secondary=table_student_course,
        backref=backref('students', uselist=True, lazy='dynamic'), lazy='dynamic')

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
    __tablename__ = "tb_nvm_course"
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
