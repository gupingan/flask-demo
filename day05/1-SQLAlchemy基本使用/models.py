import db


class Student(db.Base):
    __tablename__ = 'tb_student1'

    id = db.Column(db.Integer, primary_key=True, comment='学号')
    name = db.Column(db.String(255), comment='姓名')
    sex = db.Column(db.Boolean, comment='性别')
    age = db.Column(db.SmallInteger, comment='年龄')
    class_name = db.Column('class', db.String(32), comment='班级')
    description = db.Column(db.Text)
    description = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Student: {self.name}>'
