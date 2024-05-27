"""
Create database:
    > create database db_flask_demo_school charset=utf8mb4
"""
from sqlalchemy import *
from sqlalchemy.orm import *

# 创建连接引擎
engine = create_engine(
    url='mysql+pymysql://root:0908@localhost:3306/db_flask_demo_school?charset=utf8mb4',
    echo=True,  # 当设置为True时会将orm语句转化为sql语句打印，一般debug的时候可用
    pool_size=8,  # 连接池的大小，默认为5个，设置为0时表示连接无限制
    pool_recycle=30 * 60  # 设置时间以限制数据库多久没连接自动断开
)
# print('Engine:', engine)

# 1.4 方式
# 创建会话
# db_Session = sessionmaker(bind=engine)
# session = db_Session()
# print(session)  # <sqlalchemy.orm.session.Session object at 0x0000023663504CA0>

# 第一种基类创建方式(推荐)
# Base = declarative_base()
# print(Base)  # <class 'sqlalchemy.orm.decl_api.Base'>
# 第二种基类创建方式
# mapper_registry = registry()
# Base = mapper_registry.generate_base()
# print(Base)  # <class 'sqlalchemy.orm.decl_api.Base'>


# 2.0 方式
# 创建会话
session = Session(bind=engine)


# print(session)  # <sqlalchemy.orm.session.Session object at 0x0000020779055640>


# 基类创建方式(推荐)
class Base(DeclarativeBase):
    pass

# print(Base)  # <class '__main__.Base'>
