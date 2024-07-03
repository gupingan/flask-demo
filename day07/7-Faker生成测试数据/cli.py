import random
import click
from faker import Faker
from flask import Flask
from models import Student, SQLAlchemy

faker = Faker(locale='ZH_CN')


def init_app(app: Flask, db: SQLAlchemy):
    @app.cli.command('faker-student')
    @click.option('-n', '--number', 'number', type=int, default=10, help='指定生成学生数量')
    def faker_students(number):
        db.drop_all()
        db.create_all()
        data_list = []
        for i in range(number):
            sex = bool(random.randint(0, 1))
            student = Student(
                name=faker.name_male() if sex else faker.name_female(),
                age=random.randint(15, 40),
                sex=sex,
                email=faker.free_email(),
                create_time=faker.date_time()
            )
            data_list.append(student)

        db.session.add_all(data_list)
        db.session.commit()
