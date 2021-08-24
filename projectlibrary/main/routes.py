from flask import render_template, url_for, flash, redirect, Blueprint, request
from flask_login import login_user, logout_user, current_user, login_required
from projectlibrary import app, db, bcrypt
from projectlibrary.models import *


main = Blueprint('main', __name__)

@main.route("/", methods=['POST', 'GET'])
@main.route("/home", methods=['POST', 'GET'])
@main.route("/index", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['psw']
        
        student = Students.query.filter_by(username=username).first()
        lecturer = Lecturers.query.filter_by(username=username).first()
        #update to hashpassword and lecturer login
        if student:
            if student.password == password:
                login_user(student)
                return redirect(url_for('students.dashboard'))
            else:
                flash('Wrong username/password combination', 'warning')
        elif lecturer:
            if lecturer.password == password:
                login_user(lecturer)
                return lecturer.username
            else:
                flash('Wrong username/password combination', 'warning')
                
        else:
            flash('Wrong username/password combination', 'warning')
    return render_template("Index.html")



@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))