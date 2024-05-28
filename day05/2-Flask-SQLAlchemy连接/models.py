from db import db


class Student(db.Model):
    __tablename__ = 'tb_student2'

    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), index=True, comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), unique=True, comment="邮箱地址")
    money = db.Column(db.Numeric(10, 2), default=0.0, comment="钱包")

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}>'


class Course(db.Model):
    __tablename__ = "tb_course2"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(255), unique=True, comment="课程")
    price = db.Column(db.Numeric(8, 2), comment="价格")

    def __repr__(self):  # 相当于django的__str__
        return f"<{self.__class__.__name__}: {self.name}>"


class Teacher(db.Model):
    __tablename__ = "tb_teacher2"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(255), unique=True, comment="姓名")
    option = db.Column(db.Enum("讲师", "助教", "班主任"), default="讲师")

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name}>"
