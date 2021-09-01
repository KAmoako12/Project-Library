from datetime import datetime
from flask_login import UserMixin
from projectlibrary import db, login_manager, app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import uuid


@login_manager.user_loader
def load_user(user_id):
    student = Students.query.get(user_id)
    lecturer = Lecturers.query.get(user_id)
    
    if student:
        return Students.query.get(str(user_id))
    
    if lecturer:
        return Lecturers.query.get(str(user_id))


class User(db.Model, UserMixin):
    __abstract__ = True
    id =  db.Column(db.String(20),  primary_key=True, default=str(uuid.uuid4())[:8])
    username = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    college = db.Column(db.String(255), nullable=False)
    
    
class Students(User):
    index_number = db.Column(db.String(255), nullable=False, unique=True)
    program = db.Column(db.String(255), nullable=False)
    group_id = db.Column(db.String(255), nullable=False)
    group_leader = db.Column(db.Boolean, default=False)
    supervisor = db.Column(db.String(255), db.ForeignKey('lecturers.staff_id'), nullable=False)
    
    
class Lecturers(User):
    staff_id = db.Column(db.String(255), nullable=False, unique=True)
    department = db.Column(db.String(255), nullable=False)
    hod = db.Column(db.Boolean, default=False)
    
    
class Reports(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    topic = db.Column(db.String(255), db.ForeignKey('categories.name'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    group_id = db.Column(db.String(255), db.ForeignKey('students.group_id'), nullable=False)
    supervisor = db.Column(db.String(255), db.ForeignKey('lecturers.staff_id'), nullable=False)
    college = db.Column(db.String(255), nullable=False)
    image =  db.Column(db.String(255), nullable=False, default='default.jpg')
    published = db.Column(db.Boolean, default=False)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow, default=datetime.utcnow)
    abstract = db.Column(db.Text, default=None)
    introduction = db.Column(db.Text, default=None)
    literature_review = db.Column(db.Text, default=None)
    methodology = db.Column(db.Text, default=None)
    testing_and_evaluation = db.Column(db.Text, default=None)
    conclusion = db.Column(db.Text, default=None)
    full_report = db.Column(db.String(255), default=None)
    comments = db.relationship('Comments', backref='author', lazy=True)
    
    
class Comments(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    group_id = db.Column(db.String(255), nullable=False)
    report_id = db.Column(db.Integer, db.ForeignKey('reports.id'), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    sender = db.Column(db.String(20), db.ForeignKey('lecturers.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    
class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    