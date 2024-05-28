"""
This is a Flask application that provides a RESTFUL API for managing students.

The application includes the following endpoints:

- GET /students: Retrieves a list of all students.
- DELETE /students: Deletes all students.
- GET /students/<int:student_id>: Retrieves a specific student by ID.
- POST /students: Creates a new student.
- PUT /students/<int:student_id>: Updates a specific student by ID.
- DELETE /students/<int:student_id>: Deletes a specific student by ID.

The application uses SQLAlchemy to interact with a database, and the responses are
returned in JSON format.
"""
from pathlib import Path
from flask import Flask, jsonify, request
from config import Config
from models import db, Student

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    title = Path(__file__).name
    return title


@app.route('/students', methods=['GET'])
def get_students():
    # students = Student.query.all()  # 旧版本 2.x
    # 新版本 3.1.x
    students = db.session.execute(db.select(Student).where()).scalars()
    return jsonify({
        'success': True,
        'data': {
            'count': Student.query.count(),
            'students': [student.to_dict() for student in students]
        },
        'msg': 'success'
    })


@app.route('/students', methods=['DELETE'])
def delete_students():
    db.session.execute(db.delete(Student))
    db.session.commit()
    return jsonify({
        'success': True,
        'data': None,
        'msg': 'success'
    })


@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = db.session.get(Student, student_id)
    return jsonify({
        'success': True,
        'data': student.to_dict() if student else None,
        'msg': 'success'
    })


@app.route('/students', methods=['POST'])
def create_student():
    sex = request.form.get('sex')
    sex = int(sex) if sex.isdigit() else 0
    student = Student(
        name=request.form.get('name', '未知'),
        age=request.form.get('age', 0),
        sex=bool(sex),
        email=request.form.get('email', ''),
        money=request.form.get('money', 0),
    )
    if request.form.get('id', None) is not None:
        student.id = request.form['id']

    db.session.add(student)
    db.session.commit()
    return jsonify({
        'success': True,
        'data': student.to_dict(),
        'msg': 'success'
    }), 201


@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = db.session.get(Student, student_id)
    if not student:
        return jsonify({
            'success': False,
            'data': None,
            'msg': 'student not found'
        }), 404

    data = request.form
    for key, value in data.items():
        if hasattr(student, key):
            setattr(student, key, value)
    db.session.commit()
    return jsonify({
        'success': True,
        'data': student.to_dict(),
        'msg': 'success'
    })


@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = db.session.get(Student, student_id)
    if not student:
        return jsonify({
            'success': False,
            'data': None,
            'msg': 'student not found'
        }), 404

    db.session.delete(student)
    db.session.commit()
    return jsonify({
        'success': True,
        'data': student.to_dict(),
        'msg': 'success'
    })


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run('0.0.0.0', 9527)
