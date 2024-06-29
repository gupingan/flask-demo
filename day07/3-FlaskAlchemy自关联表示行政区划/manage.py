from pathlib import Path
from flask import Flask, request, jsonify
from config import Config
from models import db, Region

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    title = Path(__file__).name
    return title


@app.route('/regions', methods=['POST'])
def add_region():
    data = request.form
    name = data.get('name')
    parent_id = data.get('parent_id', type=int)
    if not name:
        return jsonify({'error': 'Name is required'}), 400

    region = Region(name=name, parent_id=parent_id)
    db.session.add(region)
    db.session.commit()
    return jsonify(region.to_dict()), 201


@app.route('/regions', methods=['GET'])
def get_regions():
    q = db.select(Region)
    regions = db.session.execute(q).scalars()
    return jsonify([region.to_dict() for region in regions])


@app.route('/regions/<int:region_id>', methods=['PUT'])
def update_region(region_id):
    data = request.form
    q = db.select(Region).where(Region.id == region_id)
    region = db.session.execute(q).scalar()
    if not region:
        return jsonify({'error': 'Region not found'}), 404

    name = data.get('name')
    parent_id = data.get('parent_id')

    if name:
        region.name = name
    if parent_id is not None:
        region.parent_id = parent_id

    db.session.commit()
    return jsonify(region.to_dict())


@app.route('/regions/<int:region_id>', methods=['DELETE'])
def delete_region(region_id):
    q = db.select(Region).where(Region.id == region_id)
    region = db.session.execute(q).scalar()
    if not region:
        return jsonify({'error': 'Region not found'}), 404
    db.session.delete(region)
    db.session.commit()
    return jsonify({'message': 'Region deleted successfully'})


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run('0.0.0.0', 9527)
