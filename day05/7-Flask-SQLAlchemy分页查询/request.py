# request.py
import requests  # pip install requests

students = [  # 虚拟数据，务必当真
    {
        'name': '王毅',
        'age': 21,
        'sex': 1,
        'email': 'wangyi@gmail.com',
        'money': 4488.5
    },
    {
        'name': '张晓',
        'age': 19,
        'sex': 0,
        'email': 'zhangxiao@example.com',
        'money': 2389.75
    },
    {
        'name': '李春阳',
        'age': 23,
        'sex': 1,
        'email': 'lichunyang@outlook.com',
        'money': 6715.32
    },
    {
        'name': '刘瑞',
        'age': 20,
        'sex': 0,
        'email': 'liurui@yahoo.com',
        'money': 3456.89
    },
    {
        'name': '陈欢',
        'age': 22,
        'sex': 1,
        'email': 'chenhuan@gmail.com',
        'money': 5678.12
    },
    {
        'name': '吴娜',
        'age': 18,
        'sex': 0,
        'email': 'wuna@example.org',
        'money': 1234.56
    },
    {
        'name': '赵丹',
        'age': 24,
        'sex': 0,
        'email': 'zhaoda@outlook.com',
        'money': 7890.43
    },
    {
        'name': '孙宇',
        'age': 21,
        'sex': 1,
        'email': 'sunyu@yahoo.co.jp',
        'money': 4567.89
    },
    {
        'name': '黄宇',
        'age': 19,
        'sex': 1,
        'email': 'huangyu@gmail.com',
        'money': 2345.67
    },
    {
        'name': '杨静',
        'age': 22,
        'sex': 0,
        'email': 'yangjing@example.com',
        'money': 6789.01
    }
]
for student in students:
    response = requests.request('POST', 'http://127.0.0.1:9527/students', data=student)
    print('添加一条记录', response.json())
