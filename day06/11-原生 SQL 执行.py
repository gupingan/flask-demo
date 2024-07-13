import db
from model import Student


def run():
    # DDL 读取数据
    # 返回游标对象
    cursor = db.session.execute(db.text('select * from tb_student'))
    print(cursor)
    # 获取一条结果，mappings 方法将结果转为字典
    cursor = db.session.execute(db.text('select * from tb_student'))
    print(cursor.mappings().fetchone())
    # 获取指定数量的结果
    cursor = db.session.execute(db.text('select * from tb_student'))
    print(cursor.mappings().fetchmany(2))
    # 获取所有结果
    cursor = db.session.execute(db.text('select * from tb_student'))
    print(cursor.mappings().fetchall())

    # DML 写入数据
    sql = db.text(
        'insert into tb_student(name, class, age, sex, description) values(:name, :class_, :age, :sex, :description)'
    )
    data = dict(
        name='李小白',
        age=17,
        sex=True,
        class_=1,
        description='大河之剑天上来',
    )
    cursor = db.session.execute(sql, params=data)
    db.session.commit()
    print(cursor.lastrowid)


if __name__ == '__main__':
    run()
