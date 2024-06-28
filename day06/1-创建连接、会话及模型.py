"""
>>> from sqlalchemy import create_engine
>>> from sqlalchemy.orm import sessionmaker, declarative_base

# 1.创建数据库驱动引擎
>>> engine = create_engine(
>>>     # url = '驱动://账户:密码@地址:端口/数据库名?charset=编码'
>>>     url='mysql+pymysql://root:0908@localhost:3306/db_flask_demo_school?charset=utf8mb4',
>>>     echo=True,
>>>     pool_size=8,  # 连接池的数据库连接数量
>>>     max_overflow=30,  # 连接池的数据库连接最大数量
>>>     pool_recycle=60 * 30,  # 设置秒数限制数据库多久没连接自动断开
>>> )

# 2.基于底层数据库驱动建立数据库连接会话
>>> session = sessionmaker(bind=engine)()
# 3.模型对象基类，提供数据库的基操和方法
>>> Model = declarative_base()
"""
import db
import datetime


# 创建模型
class Student(db.Model):
    # 关联数据表表名
    __tablename__ = 'tb_student'
    # 主键默认有自增 autoincrement='auto'
    id = db.Column(db.Integer, primary_key=True, comment='学生编号')
    name = db.Column(db.String(20), comment='学生姓名')
    sex = db.Column(db.Boolean, default=True, comment='学生性别')
    age = db.Column(db.SmallInteger, comment='学生年龄')
    class_ = db.Column('class', db.SMALLINT, comment='学生班级')
    description = db.Column(db.Text, comment='个性签名')
    status = db.Column(db.Boolean, default=1, comment='登录状态')
    # 日期时间字段默认值不能直接调用方法，而是方法名，比如 datetime.datetime.now
    addtime = db.Column(db.DateTime, default=datetime.datetime.now, comment='入学时间')
    orders = db.Column(db.SMALLINT, default=1, comment='学生排序')

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}({self.id})>'

    def to_dict(self):
        """
        将可显的数据转为字典
        :return:
        """
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


if __name__ == '__main__':
    # 存在 DBA Engineer，则无需创建表
    db.Model.metadata.create_all(db.engine)
