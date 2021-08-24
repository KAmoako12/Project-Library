from flask import render_template, url_for, flash, redirect, Blueprint, request, make_response
from flask_login import login_user, logout_user, current_user, login_required
from projectlibrary import app, db, bcrypt
from projectlibrary.models import *
import os
import logging

admin = Blueprint('admin', __name__)


@admin.route("/", methods=['POST', 'GET'])
@admin.route("/dashboard", methods=['POST', 'GET'])
def dashboard():
    admin_username = 'admin'
    admin_password = 'admin'

    if request.authorization and (request.authorization.username == admin_username and request.authorization.password == admin_password):
        # change to pagination
        students = Students.query.all()
        lecturers = Lecturers.query.all()
        return render_template('admin-dashboard.html', title="Super Admin Dashboard", students=students, lecturers=lecturers)

    logging.warn(request.__dict__)
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})



@admin.route("/categories", methods=['POST', 'GET'])
def category_list():
    admin_username = 'admin'
    admin_password = 'admin'

    if request.authorization and (request.authorization.username == admin_username and request.authorization.password == admin_password):
        return render_template('admin-categories.html', title="Super Admin Dashboard")

    logging.warn(request.__dict__)
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})



@admin.route("/add/new-student", methods=['POST', 'GET'])
def create_student():
    admin_username = 'admin'
    admin_password = 'admin'

    if request.authorization and (request.authorization.username == admin_username and request.authorization.password == admin_password):
        if request.method == 'POST':
            name = request.form['name']
            username = request.form['username']
            email = request.form['email']
            index_number = request.form['indexnumber']
            group_id = request.form['groupid']
            password = request.form['password']
            college = request.form['college']
            program = request.form['programme']
            
            new_student = Students(username=username, name=name, email=email, password=password, index_number=index_number,
                                  program=program, group_id=group_id)
            
            db.session.add(new_student)
            
            try:
                db.session.commit()
                flash('New Student Added!', 'success')
                return redirect(url_for('admin.dashboard'))
            except:
                flash('Some of your credentials have been used', 'warning')
            
        return render_template('create-student.html', title="Super Admin Dashboard")

    logging.warn(request.__dict__)
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})


@admin.route("/edit-student/<student_id>", methods=['POST', 'GET'])
def edit_student(student_id):
    admin_username = 'admin'
    admin_password = 'admin'
    student = Students.query.filter_by(id=student_id).first()

    if request.authorization and (request.authorization.username == admin_username and request.authorization.password == admin_password):
        if request.method == 'POST':
            name = request.form['name']
            username = request.form['username']
            email = request.form['email']
            index_number = request.form['indexnumber']
            group_id = request.form['groupid']
            password = request.form['password']
            college = request.form['college']
            program = request.form['programme']
            
            
            
            student.name = name
            student.username = username
            student.email = email
            student.index_number = index_number
            student.group_id = group_id
            student.password = password
            student.program = program
            
            try:
                db.session.commit()
                flash('Student Updated!', 'success')
                return redirect(url_for('admin.dashboard'))
            except:
                flash('Some of your credentials have been used', 'warning')
            
        return render_template('edit-student.html', title="Super Admin Dashboard", student=student)

    logging.warn(request.__dict__)
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})


@admin.route("/add/new-lecturer", methods=['POST', 'GET'])
def create_lecturer():
    admin_username = 'admin'
    admin_password = 'admin'

    if request.authorization and (request.authorization.username == admin_username and request.authorization.password == admin_password):
        if request.method == 'POST':
            name = request.form['name']
            username = request.form['username']
            email = request.form['email']
            staff_id = request.form['staffid']
            password = request.form['password']
            college = request.form['college']
            hod = request.form['hod']
            department = request.form['department']
            
            if hod == "1":
                new_lecturer = Lecturers(username=username, name=name, email=email, password=password, staff_id=staff_id,
                                  department=department, hod=True)
            else:
                new_lecturer = Lecturers(username=username, name=name, email=email, password=password, staff_id=staff_id,
                                  department=department)
            
            db.session.add(new_lecturer)
            
            try:
                db.session.commit()
                flash('New Lecturer Added!', 'success')
                return redirect(url_for('admin.dashboard'))
            except:
                flash('Some of your credentials have been used', 'warning')
        return render_template('create-lecturer.html', title="Super Admin Dashboard")

    logging.warn(request.__dict__)
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})


@admin.route("/edit-lecturer/<lecturer_id>", methods=['POST', 'GET'])
def edit_lecturer(lecturer_id):
    admin_username = 'admin'
    admin_password = 'admin'
    lecturer = Lecturers.query.filter_by(id=lecturer_id).first()

    if request.authorization and (request.authorization.username == admin_username and request.authorization.password == admin_password):
        if request.method == 'POST':
            name = request.form['name']
            username = request.form['username']
            email = request.form['email']
            staff_id = request.form['staffid']
            password = request.form['password']
            college = request.form['college']
            hod = request.form['hod']
            department = request.form['department']
            
            
            lecturer.name = name
            lecturer.username = username
            lecturer.email = email
            lecturer.staff_id = staff_id
            lecturer.password = password
            if hod == '1':
                lecturer.hod = True
            else:
                lecturer.hod = False
            lecturer.department = department
            
            try:
                db.session.commit()
                flash('New Lecturer Added!', 'success')
                return redirect(url_for('admin.dashboard'))
            except:
                flash('Some of your credentials have been used', 'warning')
        return render_template('edit-lecturer.html', title="Super Admin Dashboard", lecturer=lecturer)

    logging.warn(request.__dict__)
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})


@admin.route("/delete-user/<user_id>", methods=['POST', 'GET'])
def delete_user(user_id):
    admin_username = 'admin'
    admin_password = 'admin'

    if request.authorization and (request.authorization.username == admin_username and request.authorization.password == admin_password):
        student = Students.query.filter_by(id=user_id).first()
        lecturer = Lecturers.query.filter_by(id=user_id).first()
        if student:
            #make sure deletion is cascading for it
            db.session.delete(student)
            db.session.commit()
        elif lecturer:
            #make sure deletion is cascading
            db.session.delete(lecturer)
            db.session.commit()
        else:
            flash('No User like that exists!', 'info')
            
        return redirect(url_for('admin.dashboard'))

    logging.warn(request.__dict__)
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})