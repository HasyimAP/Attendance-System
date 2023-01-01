from . import db
from flask_login import UserMixin

# class Students(db.Model, UserMixin):
#     student_id = db.Column(db.Integer, primary_key=True, nullable=False)
#     name = db.Column(db.String(100), nullable=False)
#     batch = db.Column(db.Integer, nullable=False)
#     semester = db.Column(db.Integer, nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)

# class Teachers(db.Model, UserMixin):
#     teacher_id = db.Column(db.Integer, primary_key=True, nullable=False)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)
    
# class Admins(db.Model, UserMixin):
#     admin_id = db.Column(db.Integer, primary_key=True, nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)

class Users(db.Model, UserMixin):
    db_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100))
    batch = db.Column(db.Integer)
    semester = db.Column(db.Integer)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    
    def get_id(self):
        return self.db_id
    
class Attendances(db.Model):
    att_id = db.Column(db.Integer, primary_key=True, nullable=False)
    student_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    batch = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(), nullable=False)
    status = db.Column(db.String(), nullable=False)