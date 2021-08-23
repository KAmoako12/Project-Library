from datetime import datetime
from flask_login import UserMixin
from projectlibrary import db, login_manager, app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
    student = Students.query.get(user_id)
    lecturer = Lecturers.query.get(user_id)
    
    if student:
        return Students.query.get(int(user_id))
    
    if lecturer:
        return Lecturers.query.get(int(user_id))


class User(db.Model, UserMixin):
    __abstract__ = True
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    
    
class Students(User):
    id = db.Column(db.Integer,  primary_key=True)
    index_number = db.Column(db.String(255), nullable=False, unique=True)
    program = db.Column(db.String(255), nullable=False)
    group_id = db.Column(db.String(255), nullable=False)
    
    
class Lecturers(User):
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.String(255), nullable=False, unique=True)
    department = db.Column(db.String(255), nullable=False)
    hod = db.Column(db.Boolean, default=False)
    


    
    
