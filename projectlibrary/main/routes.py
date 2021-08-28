from flask import render_template, url_for, flash, redirect, Blueprint, request
from flask_login import login_user, logout_user, current_user, login_required
from projectlibrary import app, db, bcrypt
from projectlibrary.models import *


main = Blueprint('main', __name__)

@main.route("/", methods=['POST', 'GET'])
@main.route("/home", methods=['POST', 'GET'])
@main.route("/index", methods=['POST', 'GET'])
def home():
    user = current_user
    student = None
    lecturer = None
    if user.is_authenticated:
        student = Students.query.filter_by(id=user.id).first()
        lecturer = Lecturers.query.filter_by(id=user.id).first()

            
        
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['psw']
        
        student = Students.query.filter_by(username=username).first()
        lecturer = Lecturers.query.filter_by(username=username).first()
        #update to hashpassword and lecturer login
        if student:
            if bcrypt.check_password_hash(student.password, password):
                login_user(student)
                return redirect(url_for('students.dashboard'))
            else:
                flash('Wrong username/password combination', 'warning')
                
        if lecturer:
            if bcrypt.check_password_hash(lecturer.password, password):
                login_user(lecturer)
                return redirect(url_for('lecturers.dashboard'))
            else:
                flash('Wrong username/password combination', 'warning')
                
        else:
            flash('Wrong username/password combination', 'warning')
    return render_template("Index.html", student=student, lecturer=lecturer)



@main.route("/colleges", methods=['POST', 'GET'])
def colleges():
    return render_template('colleges.html', title='Colleges')


@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))