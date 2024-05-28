import time

import requests
import unittest


class FlaskTest(unittest.TestCase):
    GET = 'GET'
    POST = 'POST'
    DELETE = 'DELETE'
    PUT = 'PUT'

    def test_day02_query_string(self):
        response = requests.request(self.GET, 'http://127.0.0.1:9527/user?uid=1&fav=edit')
        print(response.text)

    def test_day02_form(self):
        payload = {
            'form_name': '小明',
            'fav': ['游泳', '搏击']
        }
        response = requests.request(self.POST, 'http://127.0.0.1:9527/form1', data=payload)
        print(response.text)

    def test_day02_json(self):
        payload = {
            'name': '小明',
            'fav': ['游泳', '搏击']
        }
        response = requests.request(self.POST, 'http://127.0.0.1:9527/json1', json=payload)
        print(response.text)

    def test_day02_file(self):
        f = open('./avatar.jpg', 'rb')
        files = {'avatar': f}
        request = requests.Request(self.POST, 'http://127.0.0.1:9527/file1', files=files)
        prepared = request.prepare()
        boundary = prepared.headers['Content-Type'].split('=')[1]
        print(f'Boundary: {boundary}')
        response = requests.Session().send(prepared)
        f.close()
        print(response.text)

    def test_day02_header(self):
        headers = {'Company': 'Manong'}
        # response = requests.request(self.POST, 'http://127.0.0.1:9527/header')
        response = requests.request(self.GET, 'http://127.0.0.1:9527/header?a=1', headers=headers)
        print(response.text)

    def test_day02_root(self):
        response = requests.request(self.GET, 'http://127.0.0.1:9527')
        print(response.text)
        print(response.status_code)
        print(response.headers)

    def test_day02_json_api(self):
        response = requests.request(self.GET, 'http://127.0.0.1:9527/json/api')
        print(response.text)
        print(response.json())
        print(response.status_code)
        print(response.headers)

    def test_day02_get_img(self):
        response = requests.request(self.GET, 'http://127.0.0.1:9527/img')
        print(response.content)
        with open('./get_img.png', 'wb') as fw:
            fw.write(response.content)
        print(response.status_code)
        print(response.headers)

    def test_day02_root_2(self):
        response1 = requests.request(self.GET, 'http://127.0.0.1:9527?token=123')
        response2 = requests.request(self.GET, 'http://127.0.0.1:9527')
        print(response1.text)
        print(response2.text)

    def test_day02_jump(self):
        response2 = requests.request(self.GET, 'http://127.0.0.1:9527/jump')
        print(response2.text)

    def test_day02_info_sms(self):
        response2 = requests.request(self.GET, 'http://127.0.0.1:9527/info')
        print(response2.text)

    def test_day02_root_3(self):
        response2 = requests.request(self.GET, 'http://127.0.0.1:9527')
        print(response2.text)
        print(response2.headers)

    def test_day02_set_cookie(self):
        response = requests.request(self.GET, 'http://127.0.0.1:9527/set_cookie')
        print(response.text)
        print(response.cookies)
        user_id = response.cookies.get('user_id')
        username = response.cookies.get('username')
        print(user_id, username)

    def test_day02_get_cookie(self):
        response = requests.request(self.GET, 'http://127.0.0.1:9527/get_cookie')
        print(response.text)
        print(response.cookies)
        user_id = response.cookies.get('user_id')
        username = response.cookies.get('username')
        print(user_id, username)

    def test_day02_del_cookie(self):
        response = requests.request(self.GET, 'http://127.0.0.1:9527/del_cookie')
        print(response.text)
        print(response.cookies)
        user_id = response.cookies.get('user_id')
        username = response.cookies.get('username')
        print(user_id, username)

    def test_day02_set_session(self):
        response = requests.request(self.GET, 'http://127.0.0.1:9527/set_session')
        print(response.text)
        print(response.cookies)
        user_id = response.cookies.get('user_id')
        username = response.cookies.get('username')
        print(user_id, username)

    def test_day02_get_session(self):
        response = requests.request(self.GET, 'http://127.0.0.1:9527/get_session')
        print(response.text)
        print(response.cookies)

    def test_day02_del_session(self):
        response = requests.request(self.GET, 'http://127.0.0.1:9527/del_session')
        print(response.text)
        print(response.cookies)

    def test_day03_global_hook(self):
        response = requests.request(self.GET, 'http://127.0.0.1:9527')
        print(response.text)
        print(response.headers)

    def test_day03_abort(self):
        response = requests.request(self.GET, 'http://127.0.0.1:9527?password=admi1n')
        print(response.text)
        print(response.headers)

    def test_day03_index(self):
        response = requests.request(self.GET, 'http://127.0.0.1:9527')
        print(response.text)
        print(response.headers)

    def test_day03_set_g_value(self):
        response1 = requests.request(self.GET, 'http://127.0.0.1:9527/set_value/9527')
        print(response1.text)
        print(response1.headers)
        response2 = requests.request(self.GET, 'http://127.0.0.1:9527/get_value')
        print(response2.text)

    def test_day03_index_template(self):
        response = requests.request(self.GET, 'http://127.0.0.1:9527')
        print(response.text)
        print(response.headers)

    def test_day03_render_template(self):
        response1 = requests.request(self.GET, 'http://127.0.0.1:9527/render_template')
        print(response1.text)
        response2 = requests.request(self.GET, 'http://127.0.0.1:9527/render_template_string')
        print(response2.text)

    def test_day04_render_template(self):
        response = requests.request(self.GET, 'http://127.0.0.1:9527')
        print(response.text)

    def test_day05_restful_api(self):
        response = requests.request(self.DELETE, 'http://127.0.0.1:9527/students')
        print('清空表格数据', response.json())

        old_payload = {
            'id': 1,
            'name': '王毅',
            'age': 21,
            'sex': 1,
            'email': 'wangyi@gmail.com',
            'money': 4488.5
        }
        response = requests.request(self.POST, 'http://127.0.0.1:9527/students', data=old_payload)
        print('添加一条记录', response.json())

        response = requests.request(self.GET, 'http://127.0.0.1:9527/students')
        print('获取所有记录', response.json())

        new_payload = {
            'money': 4488.5 + 4000,
        }
        response = requests.request(self.PUT, f'http://127.0.0.1:9527/students/{old_payload["id"]}', data=new_payload)
        print('获取更新后的记录', response.json())

        response = requests.request(self.GET, f'http://127.0.0.1:9527/students/{old_payload["id"]}')
        print('获取存在的一条记录', response.json())

        response = requests.request(self.DELETE, f'http://127.0.0.1:9527/students/{old_payload["id"]}')
        print('获取删除后的记录', response.json())

        response = requests.request(self.GET, f'http://127.0.0.1:9527/students/{old_payload["id"]}')
        print('获取不存在的一条记录', response.json())

    def test_day05_4(self):
        students = [
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
                'name': '孙梅',
                'age': 21,
                'sex': 0,
                'email': 'sunmei@yahoo.co.jp',
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
            response = requests.request(self.POST, 'http://127.0.0.1:9527/students', data=student)
            print('添加一条记录', response.json())

        response = requests.request(self.GET, 'http://127.0.0.1:9527/students/query')
        print('调用查询测试', response.json())

        response = requests.request(self.DELETE, 'http://127.0.0.1:9527/students')
        print('清空表格数据', response.json())

    def test_day05_5(self):
        students = [
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
            response = requests.request(self.POST, 'http://127.0.0.1:9527/students', data=student)
            print('添加一条记录', response.json())

        response = requests.request(self.GET, 'http://127.0.0.1:9527/students/filter')
        print('调用过滤测试', response.json())

        response = requests.request(self.DELETE, 'http://127.0.0.1:9527/students')
        print('清空表格数据', response.json())


if __name__ == '__main__':
    FlaskTest().run()
