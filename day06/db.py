from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, declarative_base, Session, DeclarativeBase

# 1.创建数据库驱动引擎
engine = create_engine(
    # url = '驱动://账户:密码@地址:端口/数据库名?charset=编码'
    url='mysql+pymysql://root:0908@localhost:3306/db_sqlalchemy_demo?charset=utf8mb4',
    echo=True,
    pool_size=8,  # 连接池的数据库连接数量
    max_overflow=30,  # 连接池的数据库连接最大数量
    pool_recycle=60 * 30,  # 设置秒数限制数据库多久没连接自动断开
)

# 2.基于底层数据库驱动建立数据库连接会话
# DBSession = sessionmaker(bind=engine)
# session = DBSession()
session = Session(bind=engine)


# 3.模型对象基类，提供数据库的基操和方法
# Model = declarative_base()
class Model(DeclarativeBase):
    pass
