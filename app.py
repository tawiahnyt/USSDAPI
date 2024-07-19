from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_user, LoginManager, login_required, current_user, logout_user, UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'jwt-secret-key'
db = SQLAlchemy(app)
jwt = JWTManager(app)


class StudentData(UserMixin, db.Model):
    __tablename__ = 'student_data'
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    other_name = db.Column(db.String(250))
    date_of_birth = db.Column(db.String(250))
    phone = db.Column(db.String(250))
    email = db.Column(db.String(250))
    student_email = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    level = db.Column(db.String(250))
    student_type = db.Column(db.String(250))
    enrollment_date = db.Column(db.String(250))
    graduation_date = db.Column(db.String(250))
    degree_programmes = db.Column(db.String(250))
    undergraduate_programmes = db.Column(db.String(250))
    guardian_name = db.Column(db.String(250))
    guardian_email = db.Column(db.String(250))
    guardian_phone = db.Column(db.String(250))
    guardian_address = db.Column(db.String(250))
    password = db.Column(db.String(250))

    def get_id(self):
        return self.student_id


class StudentResultData(UserMixin, db.Model):
    __tablename__ = 'results_data'
    student_id = db.Column(db.Integer, primary_key=True)
    MATH_173 = db.Column(db.Integer)
    MATH_171 = db.Column(db.Integer)
    FREN_171 = db.Column(db.Integer)
    IT_133 = db.Column(db.Integer)
    METS_173 = db.Column(db.Integer)
    IT_101 = db.Column(db.Integer)
    SCOT_175 = db.Column(db.Integer)
    FREN_172 = db.Column(db.Integer)
    IT_102 = db.Column(db.Integer)
    IT_124 = db.Column(db.Integer)
    IT_152 = db.Column(db.Integer)
    MATH_176 = db.Column(db.Integer)
    ENG_174 = db.Column(db.Integer)
    AFRS_271 = db.Column(db.Integer)
    IT_231 = db.Column(db.Integer)
    IT_241 = db.Column(db.Integer)
    IT_245 = db.Column(db.Integer)
    FREN_273 = db.Column(db.Integer)
    IT_221 = db.Column(db.Integer)
    ENGL_275 = db.Column(db.Integer)
    IT_206 = db.Column(db.Integer)
    IT_274 = db.Column(db.Integer)
    IT_242 = db.Column(db.Integer)
    IT_222 = db.Column(db.Integer)
    IT_232 = db.Column(db.Integer)
    IT_204 = db.Column(db.Integer)
    IT_276 = db.Column(db.Integer)
    IT_323 = db.Column(db.Integer)
    IT_343 = db.Column(db.Integer)
    IT_313 = db.Column(db.Integer)
    IT_371 = db.Column(db.Integer)
    IT_391 = db.Column(db.Integer)
    IT_305 = db.Column(db.Integer)
    IT_301 = db.Column(db.Integer)
    IT_308 = db.Column(db.Integer)
    IT_302 = db.Column(db.Integer)
    IT_324 = db.Column(db.Integer)
    IT_344 = db.Column(db.Integer)
    IT_306 = db.Column(db.Integer)


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(student_id):
    return StudentData.query.get(int(student_id))


with open('courses.json') as file:
    data = json.load(file)


# @app.route('/', methods=['POST'])
# def login():
#     data = request.json
#     username = data.get('username')
#     password = data.get('password')
#
#     student = StudentData.query.filter_by(student_id=username).first()
#
#     if not student:
#         return jsonify({'error': 'Student ID not found, please try again'}), 404
#     if not check_password_hash(student.password, password):
#         return jsonify({'error': 'Incorrect password, please try again'}), 401
#
#     user = {
#         username: student,
#         password: check_password_hash(student.password, password)
#     }
#     # login_user(student)
#     # return jsonify({'message': 'Logged in successfully'}), 200
#     # access_token = create_access_token(identity=username)
#     # return jsonify(access_token=access_token), 200
#
#     print(jsonify(user))
#     return jsonify(user)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    student = StudentData.query.filter_by(student_id=username).first()

    if not student:
        return jsonify({'error': 'Student ID not found, please try again'}), 404
    if not check_password_hash(student.password, password):
        return jsonify({'error': 'Incorrect password, please try again'}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    if request.method == 'GET':
        account_data = {
            'student_id': current_user.student_id,
            'first_name': current_user.first_name,
            'last_name': current_user.last_name,
            'other_name': current_user.other_name,
            'date_of_birth': current_user.date_of_birth,
            'phone': current_user.phone,
            'email': current_user.email,
            'student_email': current_user.student_email,
            'gender': current_user.gender,
            'level': current_user.level,
            'student_type': current_user.student_type,
            'enrollment_date': current_user.enrollment_date,
            'graduation_date': current_user.graduation_date,
            'degree_programmes': current_user.degree_programmes,
            'guardian_name': current_user.guardian_name,
            'guardian_email': current_user.guardian_email,
            'guardian_phone': current_user.guardian_phone,
            'guardian_address': current_user.guardian_address,
        }
        return jsonify(account_data), 200

    data = request.json
    form_name = data.get('form_name')

    if form_name == 'change_password':
        password = data.get('password')
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        if not check_password_hash(current_user.password, password):
            return jsonify({'error': 'Current password is incorrect, please try again'}), 400
        if new_password != confirm_password:
            return jsonify({'error': 'New passwords do not match, please try again'}), 400

        current_user.password = generate_password_hash(new_password)
        db.session.commit()
        return jsonify({'message': 'Password changed successfully'}), 200

    if form_name == 'update_details':
        contact_name = data.get('contact_name')
        contact_mobile = data.get('contact_mobile')
        contact_email = data.get('contact_email')
        contact_address = data.get('contact_address')
        alternative_email = data.get('alternative_email')
        additional_contact_email = data.get('additional_contact_email')

        if contact_name:
            current_user.emergency_contact_name = contact_name
        if contact_mobile:
            current_user.emergency_contact_mobile = contact_mobile
        if contact_email:
            current_user.emergency_contact_email = contact_email
        if contact_address:
            current_user.emergency_contact_address = contact_address
        if alternative_email:
            current_user.alternative_email = alternative_email
        if additional_contact_email:
            current_user.additional_contact_email = additional_contact_email

        db.session.commit()
        return jsonify({'message': 'Emergency contact information updated successfully'}), 200


@app.route('/courses', methods=['GET'])
@login_required
def courses():
    student_courses = data[current_user.degree_programmes][current_user.level]['first_semester']
    return jsonify(student_courses), 200


@app.route('/results', methods=['GET'])
@login_required
def results():
    student_results = db.session.query(StudentResultData).filter_by(student_id=current_user.student_id).first()
    if not student_results:
        return jsonify({'error': 'Results not found'}), 404

    results_data = {
        'student_id': student_results.student_id,
        'MATH_173': student_results.MATH_173,
        'MATH_171': student_results.MATH_171,
        'FREN_171': student_results.FREN_171,
        'IT_133': student_results.IT_133,
        'METS_173': student_results.METS_173,
        'IT_101': student_results.IT_101,
        'SCOT_175': student_results.SCOT_175,
        'FREN_172': student_results.FREN_172,
        'IT_102': student_results.IT_102,
        'IT_124': student_results.IT_124,
        'IT_152': student_results.IT_152,
        'MATH_176': student_results.MATH_176,
        'ENG_174': student_results.ENG_174,
        'AFRS_271': student_results.AFRS_271,
        'IT_231': student_results.IT_231,
        'IT_241': student_results.IT_241,
        'IT_245': student_results.IT_245,
        'FREN_273': student_results.FREN_273,
        'IT_221': student_results.IT_221,
        'ENGL_275': student_results.ENGL_275,
        'IT_206': student_results.IT_206,
        'IT_274': student_results.IT_274,
        'IT_242': student_results.IT_242,
        'IT_222': student_results.IT_222,
        'IT_232': student_results.IT_232,
        'IT_204': student_results.IT_204,
        'IT_276': student_results.IT_276,
        'IT_323': student_results.IT_323,
        'IT_343': student_results.IT_343,
        'IT_313': student_results.IT_313,
        'IT_371': student_results.IT_371,
        'IT_391': student_results.IT_391,
        'IT_305': student_results.IT_305,
        'IT_301': student_results.IT_301,
        'IT_308': student_results.IT_308,
        'IT_302': student_results.IT_302,
        'IT_324': student_results.IT_324,
        'IT_344': student_results.IT_344,
        'IT_306': student_results.IT_306
    }

    return jsonify(results_data), 200


@app.route('/evaluation', methods=['GET'])
@login_required
def evaluation():
    # Assuming this returns some evaluation data in JSON format
    evaluation_data = {'message': 'Evaluation endpoint'}
    return jsonify(evaluation_data), 200


if __name__ == '__main__':
    app.run(debug=True, port=4000)
