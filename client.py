import requests
import unittest


class FlaskTest(unittest.TestCase):
    GET = 'GET'
    POST = 'POST'

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


if __name__ == '__main__':
    FlaskTest().run()
