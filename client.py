import time
import random
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

        response = requests.request(self.GET, 'http://127.0.0.1:9527/students/exist/1')
        print('检查存在的数据', response.json())

        response = requests.request(self.GET, 'http://127.0.0.1:9527/students/exist/123')
        print('检查不存在的数据', response.json())

        response = requests.request(self.DELETE, 'http://127.0.0.1:9527/students')
        print('清空表格数据', response.json())

    def test_day05_6(self):
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
        response = requests.request(self.GET, 'http://127.0.0.1:9527/students/data')
        print('调用逻辑查询调试', response.text)
        response = requests.request(self.DELETE, 'http://127.0.0.1:9527/students')
        print('清空表格数据', response.json())

    def test_day05_7(self):
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
        params = {
            'page': 1,
            'size': 5,
        }
        response = requests.request(self.GET, 'http://127.0.0.1:9527/students/data', params=params)
        print('调用分页查询调试', response.text)
        # response = requests.request(self.DELETE, 'http://127.0.0.1:9527/students')
        # print('清空表格数据', response.json())

    def test_day05_8(self):
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
        response = requests.request(self.GET, 'http://127.0.0.1:9527/students/data')
        print('调用聚合分组调试', response.text)
        response = requests.request(self.DELETE, 'http://127.0.0.1:9527/students')
        print('清空表格数据', response.json())

    def test_day05_9(self):
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
            requests.request(self.POST, 'http://127.0.0.1:9527/students', data=student)
        response = requests.request(self.GET, 'http://127.0.0.1:9527/students')
        print('查询添加的所有数据', response.text)
        response = requests.request(self.GET, 'http://127.0.0.1:9527/query')
        print('调用关联查询一对一调试', response.text)
        response = requests.request(self.DELETE, 'http://127.0.0.1:9527/students')
        print('清空表格数据', response.json())

    def test_day05_10(self):
        students = [
            {
                'name': '王毅',
            },
            {
                'name': '张晓',
            },
            {
                'name': '李春阳',
            },
            {
                'name': '刘瑞',
            },
            {
                'name': '陈欢',
            },
            {
                'name': '吴娜',
            },
            {
                'name': '赵丹',
            },
            {
                'name': '孙宇',
            },
            {
                'name': '黄宇',
            },
            {
                'name': '杨静',
            }
        ]
        for student in students:
            requests.request(self.POST, 'http://127.0.0.1:9527/students', data=student)

        addresses = [
            {
                'name': '家',
                'province': '北京市',
                'city': '北京市',
                'area': '海淀区',
                'address': '中关村大街甲28号',
                'mobile': '13800138000',
            },
            {
                'name': '家',
                'province': '上海市',
                'city': '上海市',
                'area': '浦东新区',
                'address': '张江高科路588号',
                'mobile': '13900139000',
            },
            {
                'name': '家',
                'province': '广东省',
                'city': '广州市',
                'area': '天河区',
                'address': '天河北路233号',
                'mobile': '13700137000',
            },
            {
                'name': '家',
                'province': '浙江省',
                'city': '杭州市',
                'area': '西湖区',
                'address': '文三路100号',
                'mobile': '13600136000',
            },
            {
                'name': '家',
                'province': '四川省',
                'city': '成都市',
                'area': '武侯区',
                'address': '高新区天府大道1000号',
                'mobile': '13500135000',
            },
            {
                'name': '家',
                'province': '江苏省',
                'city': '南京市',
                'area': '玄武区',
                'address': '长江路88号',
                'mobile': '13400134000',
            },
            {
                'name': '家',
                'province': '湖北省',
                'city': '武汉市',
                'area': '洪山区',
                'address': '东湖高新区珞瑜路1000号',
                'mobile': '13300133000',
            },
            {
                'name': '家',
                'province': '福建省',
                'city': '厦门市',
                'area': '思明区',
                'address': '环岛路99号',
                'mobile': '13200132000',
            },
            {
                'name': '家',
                'province': '山东省',
                'city': '青岛市',
                'area': '市南区',
                'address': '香港中路200号',
                'mobile': '13100131000',
            },
            {
                'name': '家',
                'province': '辽宁省',
                'city': '大连市',
                'area': '中山区',
                'address': '中山路123号',
                'mobile': '13000130000',
            }
        ]
        for index, address in enumerate(addresses):
            response = requests.request(self.POST, f'http://127.0.0.1:9527/address?id={index + 1}', data=address)
            print('添加一条地址', response.text)
        response = requests.request(self.GET, 'http://127.0.0.1:9527/query')
        print('调用关联查询一对一调试', response.text)
        response = requests.request(self.DELETE, 'http://127.0.0.1:9527/students')
        print('清空表格数据', response.json())

    def test_day06_1(self):
        # 创建学生
        students = [
            {
                'name': '王毅',
                'age': 21,
                'sex': 1,
                'money': 4488.5
            },
            {
                'name': '张晓',
                'age': 19,
                'sex': 0,
                'money': 2389.75
            },
            {
                'name': '李春阳',
                'age': 23,
                'sex': 1,
                'money': 6715.32
            },
            {
                'name': '刘瑞',
                'age': 20,
                'sex': 0,
                'money': 3456.89
            },
            {
                'name': '陈欢',
                'age': 22,
                'sex': 1,
                'money': 5678.12
            },
            {
                'name': '吴娜',
                'age': 18,
                'sex': 0,
                'money': 1234.56
            },
            {
                'name': '赵丹',
                'age': 24,
                'sex': 0,
                'money': 7890.43
            },
            {
                'name': '孙宇',
                'age': 21,
                'sex': 1,
                'money': 4567.89
            },
            {
                'name': '黄宇',
                'age': 19,
                'sex': 1,
                'money': 2345.67
            },
            {
                'name': '杨静',
                'age': 22,
                'sex': 0,
                'money': 6789.01
            }
        ]
        for student in students:
            requests.request(self.POST, 'http://127.0.0.1:9527/students', data=student)
        # 创建课程
        courses = [
            {
                'name': 'Python入门',
                'price': 102,
            },
            {
                'name': 'Python初级',
                'price': 112,
            },
            {
                'name': 'Python进阶',
                'price': 132,
            },
            {
                'name': 'Python高级',
                'price': 200,
            },
            {
                'name': 'Python架构入门',
                'price': 210,
            }
        ]
        for course in courses:
            requests.request(self.POST, f'http://127.0.0.1:9527/courses', data=course)
        # 学生购买课程
        for index, student in enumerate(students):
            sid = index + 1
            course_len = len(courses)
            course_ids = random.choices(range(1, course_len + 1), k=random.randrange(1, course_len))
            data = {
                'sid': sid,
                'course_ids': course_ids,
            }
            requests.request(self.POST, f'http://127.0.0.1:9527/buy', data=data)

        params = {'sid': 3}
        response = requests.request(self.GET, 'http://127.0.0.1:9527/query', params=params)
        print('调用关联查询', response.json())
        response = requests.request(self.DELETE, 'http://127.0.0.1:9527/drop')
        print('清空表格数据', response.json())

    def test_day06_2(self):
        # 创建学生
        students = [
            {
                'name': '王毅',
                'age': 21,
                'sex': 1,
                'money': 4488.5
            },
            {
                'name': '张晓',
                'age': 19,
                'sex': 0,
                'money': 2389.75
            },
            {
                'name': '李春阳',
                'age': 23,
                'sex': 1,
                'money': 6715.32
            },
            {
                'name': '刘瑞',
                'age': 20,
                'sex': 0,
                'money': 3456.89
            },
            {
                'name': '陈欢',
                'age': 22,
                'sex': 1,
                'money': 5678.12
            },
            {
                'name': '吴娜',
                'age': 18,
                'sex': 0,
                'money': 1234.56
            },
            {
                'name': '赵丹',
                'age': 24,
                'sex': 0,
                'money': 7890.43
            },
            {
                'name': '孙宇',
                'age': 21,
                'sex': 1,
                'money': 4567.89
            },
            {
                'name': '黄宇',
                'age': 19,
                'sex': 1,
                'money': 2345.67
            },
            {
                'name': '杨静',
                'age': 22,
                'sex': 0,
                'money': 6789.01
            }
        ]
        for student in students:
            requests.request(self.POST, 'http://127.0.0.1:9527/students', data=student)
        # 创建课程
        courses = [
            {
                'name': 'Python入门',
                'price': 102,
            },
            {
                'name': 'Python初级',
                'price': 112,
            },
            {
                'name': 'Python进阶',
                'price': 132,
            },
            {
                'name': 'Python高级',
                'price': 200,
            },
            {
                'name': 'Python架构入门',
                'price': 210,
            }
        ]
        for course in courses:
            requests.request(self.POST, f'http://127.0.0.1:9527/courses', data=course)
        # 学生购买课程
        for index, student in enumerate(students):
            sid = index + 1
            course_len = len(courses)
            course_ids = random.choices(range(1, course_len + 1), k=random.randrange(1, course_len))
            data = {
                'sid': sid,
                'course_ids': course_ids,
            }
            requests.request(self.POST, f'http://127.0.0.1:9527/buy', data=data)

        params = {'sid': 3}
        response = requests.request(self.GET, 'http://127.0.0.1:9527/query', params=params)
        print('调用关联查询', response.json())
        # response = requests.request(self.DELETE, 'http://127.0.0.1:9527/drop')
        # print('清空表格数据', response.json())

    def test_day06_region(self):
        # TODO 增加北京市、北京市规划中的朝阳区和老朝阳区
        data = {
            'name': '北京市',
            'parent_id': None
        }
        response = requests.request(self.POST, 'http://127.0.0.1:9527/regions', data=data)
        result1 = response.json()
        print('添加北京市', result1)
        data = {
            'name': '规划中的朝阳区',
            'parent_id': result1['id'],
        }
        response = requests.request(self.POST, 'http://127.0.0.1:9527/regions', data=data)
        result2 = response.json()
        print('添加北京市的正在规划的朝阳区', result2)
        data = {
            'name': '老朝阳区',
            'parent_id': result1['id'],
        }
        response = requests.request(self.POST, 'http://127.0.0.1:9527/regions', data=data)
        result3 = response.json()
        print('添加北京市的老朝阳区', result3)

        # TODO 查询现有的区域
        response = requests.request(self.GET, f'http://127.0.0.1:9527/regions')
        result = response.json()
        print('查询所有区域', result)

        # TODO 更新北京市规划中的朝阳区为新朝阳区
        data = {
            'name': '新朝阳区',
            'parent_id': result1['id'],
        }
        response = requests.request(self.PUT, f'http://127.0.0.1:9527/regions/{result2["id"]}', data=data)
        result4 = response.json()
        print('更新原规划的朝阳区为新朝阳区', result4)

        # TODO 删除北京市原有的老朝阳区
        response = requests.request(self.DELETE, f'http://127.0.0.1:9527/regions/{result3["id"]}')
        result5 = response.json()
        print('删除北京市的老朝阳区', result5)

    def test_day06_3(self):
        # 创建学生
        students = [
            {
                'name': '王毅',
                'age': 21,
                'sex': 1,
                'money': 4488.5
            },
            {
                'name': '张晓',
                'age': 19,
                'sex': 0,
                'money': 2389.75
            },
            {
                'name': '李春阳',
                'age': 23,
                'sex': 1,
                'money': 6715.32
            },
            {
                'name': '刘瑞',
                'age': 20,
                'sex': 0,
                'money': 3456.89
            },
            {
                'name': '陈欢',
                'age': 22,
                'sex': 1,
                'money': 5678.12
            },
            {
                'name': '吴娜',
                'age': 18,
                'sex': 0,
                'money': 1234.56
            },
            {
                'name': '赵丹',
                'age': 24,
                'sex': 0,
                'money': 7890.43
            },
            {
                'name': '孙宇',
                'age': 21,
                'sex': 1,
                'money': 4567.89
            },
            {
                'name': '黄宇',
                'age': 19,
                'sex': 1,
                'money': 2345.67
            },
            {
                'name': '杨静',
                'age': 22,
                'sex': 0,
                'money': 6789.01
            }
        ]
        for student in students:
            requests.request(self.POST, 'http://127.0.0.1:9527/students', data=student)
        # 创建课程
        courses = [
            {
                'name': 'Python入门',
                'price': 102,
            },
            {
                'name': 'Python初级',
                'price': 112,
            },
            {
                'name': 'Python进阶',
                'price': 132,
            },
            {
                'name': 'Python高级',
                'price': 200,
            },
            {
                'name': 'Python架构入门',
                'price': 210,
            }
        ]
        for course in courses:
            requests.request(self.POST, f'http://127.0.0.1:9527/courses', data=course)
        # 学生购买课程
        for index, student in enumerate(students):
            sid = index + 1
            course_len = len(courses)
            course_ids = random.choices(range(1, course_len + 1), k=random.randrange(1, course_len))
            data = {
                'sid': sid,
                'course_ids': course_ids,
            }
            requests.request(self.POST, f'http://127.0.0.1:9527/buy', data=data)

        params = {'sid': 3}
        response = requests.request(self.GET, 'http://127.0.0.1:9527/query', params=params)
        print('调用关联查询', response.json())
        response = requests.request(self.DELETE, 'http://127.0.0.1:9527/drop')
        print('清空表格数据', response.json())

    def test_day06_4(self):
        # 创建学生
        students = [
            {
                'name': '王毅',
                'age': 21,
                'sex': 1,
                'money': 4488.5
            },
            {
                'name': '张晓',
                'age': 19,
                'sex': 0,
                'money': 2389.75
            },
            {
                'name': '李春阳',
                'age': 23,
                'sex': 1,
                'money': 6715.32
            },
            {
                'name': '刘瑞',
                'age': 20,
                'sex': 0,
                'money': 3456.89
            },
            {
                'name': '陈欢',
                'age': 22,
                'sex': 1,
                'money': 5678.12
            },
            {
                'name': '吴娜',
                'age': 18,
                'sex': 0,
                'money': 1234.56
            },
            {
                'name': '赵丹',
                'age': 24,
                'sex': 0,
                'money': 7890.43
            },
            {
                'name': '孙宇',
                'age': 21,
                'sex': 1,
                'money': 4567.89
            },
            {
                'name': '黄宇',
                'age': 19,
                'sex': 1,
                'money': 2345.67
            },
            {
                'name': '杨静',
                'age': 22,
                'sex': 0,
                'money': 6789.01
            }
        ]
        for student in students:
            requests.request(self.POST, 'http://127.0.0.1:9527/students', data=student)
        # 创建课程
        courses = [
            {
                'name': 'Python入门',
                'price': 102,
            },
            {
                'name': 'Python初级',
                'price': 112,
            },
            {
                'name': 'Python进阶',
                'price': 132,
            },
            {
                'name': 'Python高级',
                'price': 200,
            },
            {
                'name': 'Python架构入门',
                'price': 210,
            }
        ]
        for course in courses:
            requests.request(self.POST, f'http://127.0.0.1:9527/courses', data=course)
        # 学生购买课程
        for index, student in enumerate(students):
            sid = index + 1
            course_len = len(courses)
            course_ids = random.choices(range(1, course_len + 1), k=random.randrange(1, course_len))
            data = {
                'sid': sid,
                'course_ids': course_ids,
            }
            requests.request(self.POST, f'http://127.0.0.1:9527/buy', data=data)

        params = {'sid': 3}
        response = requests.request(self.GET, 'http://127.0.0.1:9527/query', params=params)
        print('调用关联查询', response.json())
        response = requests.request(self.DELETE, 'http://127.0.0.1:9527/drop')
        print('清空表格数据', response.json())


if __name__ == '__main__':
    unittest.main()
