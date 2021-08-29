from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, HiddenField, RadioField, FormField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from projectlibrary.models import *


class NewStudentForm(FlaskForm):
    name = StringField('Student Name', validators=[DataRequired(), Length(min=3)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    group_id = StringField('Group ID', validators=[DataRequired()])
    staff_id = StringField('Supervisor Staff ID', validators=[DataRequired()])
    group_leader = SelectField('Group Leader', choices=[('0', 'No'), ('1', 'Yes')])
    password = StringField('Password', validators=[DataRequired(), Length(min=5)])
    college = SelectField('College', choices=[('Engineering', 'College of Engineering'), ('Sciences', 'College of Science'),
                                             ('Health Sciences', ' College of Health Sciences'), ('Cabe', 'College of Art and Built Environment'),
                                             ('Humanities', 'College of Humanities'), ('Natural Resources', 'College of Agriculture and Natural Resources')])
    programme = StringField('Programme', validators=[DataRequired()])
    submit = SubmitField('Add Student')
    
    
    def validate_username(self, username):
        student = Students.query.filter_by(username=username.data).first()
        lecturer = Lecturers.query.filter_by(username=username.data).first()
        
        if student or lecturer:
            raise ValidationError('This Username has been taken!')
            
    
    def validate_email(self, email):
        student = Students.query.filter_by(email=email.data).first()
        lecturer = Lecturers.query.filter_by(email=email.data).first()
        
        if student or lecturer:
            raise ValidationError('This Email has been taken!')