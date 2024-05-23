from flask import Flask

app = Flask(__name__)


@app.route(rule='/', methods=['GET', 'POST'])
def index():
    return 'Hello Flask'


"""
DEFAULT_CONVERTERS: t.Mapping[str, type[BaseConverter]] = {
    "default": UnicodeConverter,
    "string": UnicodeConverter,
    "any": AnyConverter,
    "path": PathConverter,
    "int": IntegerConverter,
    "float": FloatConverter,
    "uuid": UUIDConverter,
}
"""
from werkzeug.routing.converters import BaseConverter


class MobileConverter(BaseConverter):
    regex = r'(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}'


app.url_map.converters['mobile'] = MobileConverter


@app.route('/user/mobile/<mobile:number>')
def mobile(number):
    return f"查询手机号码：{number}"


class RegexConverter(BaseConverter):
    def __init__(self, map, regex, *args, **kwargs):
        super().__init__(map, *args, **kwargs)
        self.regex = regex


app.url_map.converters['regex'] = RegexConverter


@app.route('/test_regex/<regex("[+-]?\d+"):num>')
def test_regex(num):
    print(num, type(num))
    return f'{num}'


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
