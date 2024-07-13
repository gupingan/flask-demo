import datetime
import db


class Student(db.Model):
    __tablename__ = 'tb_student'
    id = db.Column(db.Integer, primary_key=True, comment='学生编号')
    name = db.Column(db.String(20), comment='学生姓名')
    sex = db.Column(db.Boolean, default=True, comment='学生性别')
    age = db.Column(db.SmallInteger, comment='学生年龄')
    class_ = db.Column('class', db.SMALLINT, comment='学生班级')
    description = db.Column(db.Text, comment='个性签名')
    status = db.Column(db.Boolean, default=True, comment='登录状态')
    addtime = db.Column(db.DateTime, default=datetime.datetime.now, comment='入学时间')
    orders = db.Column(db.SMALLINT, default=True, comment='学生排序')

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}({self.id})>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'sex': self.sex,
            'age': self.age,
            'class': self.class_,
            'description': self.description,
            'status': self.status,
            'addtime': self.addtime.strftime('%Y-%m-%d %H:%M:%S'),
            'orders': self.orders,
        }
