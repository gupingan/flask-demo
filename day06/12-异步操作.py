import asyncio
import datetime
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import *

# 1.创建数据库驱动引擎
engine = create_async_engine(
    # 异步下，需要安装 aiomysql
    url='mysql+aiomysql://root:0908@localhost:3306/db_sqlalchemy_demo?charset=utf8mb4',
    echo=True,
    pool_size=10,
    max_overflow=30,
    pool_recycle=60 * 30,
)

# 2.创建异步会话类
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


# 3.创建模型基类
class Model(DeclarativeBase):
    pass


# 4.创建模型
class Student(Model):
    __tablename__ = "tb_async_student"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    sex = Column(Boolean, default=True)
    age = Column(SmallInteger)
    class_ = Column("class", SMALLINT)
    description = Column(Text)
    status = Column(Boolean, default=1)
    addtime = Column(DateTime, default=datetime.datetime.now)
    orders = Column(SMALLINT, default=1)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name}>"

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


async def main():
    async with engine.begin() as conn:
        # 删除当前程序中所有的模型对应的数据表
        await conn.run_sync(Model.metadata.drop_all)
        # 创建当前程序中所有的模型的数据表，如果数据表不存在的情况下
        await conn.run_sync(Model.metadata.create_all)

    async with async_session() as session:
        async with session.begin():
            """DML - 写入数据"""
            student1 = Student(name="小明1号", class_="302", sex=True, age=18, description="滚出去..")
            student2 = Student(name="小明2号", class_="303", sex=True, age=18, description="滚出去..")
            student3 = Student(name="小明3号", class_="305", sex=True, age=18, description="滚出去..")
            student4 = Student(name="小明4号", class_="305", sex=True, age=18, description="滚出去..")
            # 添加一条数据
            session.add(student1)
            # 添加多条数据
            session.add_all([student1, student2, student3, student4])

    async with async_session() as session:
        async with session.begin():
            """DQL - 查询数据"""
            # 拼接SQL语句
            q = select(Student).where(Student.class_ == 305).order_by(Student.id)
            print(q)
            # 异步执行SQL语句
            student = await session.execute(q)
            # 获取一个结果
            print(student.scalar().to_dict())
            # 获取多个结果
            student = await session.execute(q)
            print(list(student.scalars()))


if __name__ == '__main__':
    # asyncio.run(main())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
