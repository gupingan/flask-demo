from flask import Flask

app = Flask(__name__)


@app.route(rule='/', methods=['GET', 'POST'])
def index():
    return 'Hello Flask'


@app.route('/goods/<cid>/<int:id>')
def goods(cid, id):
    print(cid, type(cid))
    print(id, type(id))
    return f'<br>{cid}-{id}</br>'


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


if __name__ == '__main__':
    app.run('0.0.0.0', 9527, debug=True)
