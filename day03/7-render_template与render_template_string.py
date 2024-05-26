from flask import Flask, render_template, render_template_string

app = Flask(__name__, template_folder='templates')


@app.route('/render_template', methods=['GET'])
def index1():
    title = '主页1'
    content1 = 'This is a content1'
    html = render_template('index.html', **locals())
    print(html, type(html))  # 实际上渲染出来的是字符串类型，也就是html 内容
    return html


@app.route('/render_template_string', methods=['GET'])
def index2():
    title = '主页2'
    content1 = 'This is a content1'
    raw_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{title}}</title>
</head>
<body>
<h1>{{title}}</h1>
<div>{{content1}}</div>
</body>
</html>"""
    return render_template_string(raw_html, **locals())


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
