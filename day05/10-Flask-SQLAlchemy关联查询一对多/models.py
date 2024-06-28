from db import *


class Student(db.Model):
    __tablename__ = 'tb_1vn_student'

    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), index=True, comment="姓名")

    addresses = db.relationship('StudentAddress', uselist=True,
                                backref=backref('student', uselist=False), lazy='subquery')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}>'


class StudentAddress(db.Model):
    __tablename__ = 'tb_1vn_student_info'

    id = db.Column(db.Integer, primary_key=True, comment='主键')
    name = db.Column(db.String(50), default="默认", comment="地址名称")
    province = db.Column(db.String(50), comment="省份")
    city = db.Column(db.String(50), comment="城市")
    area = db.Column(db.String(50), comment="地区")
    address = db.Column(db.String(500), comment="详细地址")
    mobile = db.Column(db.String(15), comment="收货人电话")

    stu_id = db.Column(db.Integer, db.ForeignKey('tb_1vn_student.id'), comment='student外键')
    # student = db.relationship('Student', uselist=False, backref=backref('addresses', uselist=True, lazy='subquery'))

    def to_dict(self):
        info = {
            'id': self.id,
            'address_name': self.name,
            'province': self.province,
            'city': self.city,
            'area': self.area,
            'address': self.address,
            'mobile': self.mobile,
        }
        return info

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.student.name}>'
