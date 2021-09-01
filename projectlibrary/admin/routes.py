from flask import render_template, url_for, flash, redirect, Blueprint, request, make_response
from flask_login import login_user, logout_user, current_user, login_required
from projectlibrary import app, db, bcrypt
from projectlibrary.models import *
from projectlibrary.forms import NewStudentForm
from sqlalchemy import or_
import os
import logging
import uuid

admin = Blueprint('admin', __name__)


@admin.route("/", methods=['POST', 'GET'], defaults={'page':1})
@admin.route("/dashboard", methods=['POST', 'GET'], defaults={'page':1})
@admin.route("/dashboard/<int:page>", methods=['POST', 'GET'])
def dashboard(page):
    admin_username = 'admin'
    admin_password = 'admin'

    if request.authorization and (request.authorization.username == admin_username and request.authorization.password == admin_password):
        # change to pagination
        students = Students.query.paginate(page=page, per_page=5)
        
        next_url = url_for('admin.dashboard', page=students.next_num) \
            if students.has_next else None
        
        prev_url = url_for('admin.dashboard', page=students.prev_num) \
            if students.has_prev else None
        return render_template('admin-dashboard.html', title="Super Admin Dashboard", students=students, next_url=next_url, prev_url=prev_url)

    logging.warn(request.__dict__)
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})



@admin.route("/lecturers", methods=['POST', 'GET'], defaults={'page':1})
@admin.route("/lecturers/<int:page>", methods=['POST', 'GET'])
def lecturers(page):
    admin_username = 'admin'
    admin_password = 'admin'

    if request.authorization and (request.authorization.username == admin_username and request.authorization.password == admin_password):
        # change to pagination
        lecturers = Lecturers.query.paginate(page=page, per_page=5)
        
        next_url = url_for('admin.lecturers', page=lecturers.next_num) \
            if lecturers.has_next else None
        
        prev_url = url_for('admin.lecturers', page=lecturers.prev_num) \
            if lecturers.has_prev else None
        return render_template('show-lecturers.html', title="Super Admin Dashboard", lecturers=lecturers)

    logging.warn(request.__dict__)
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})



@admin.route("/categories", methods=['POST', 'GET'], defaults={'page':1})
@admin.route("/categories/<int:page>", methods=['POST', 'GET'])
def category_list(page):
    admin_username = 'admin'
    admin_password = 'admin'

    if request.authorization and (request.authorization.username == admin_username and request.authorization.password == admin_password):
        categories = Categories.query.paginate(page=page, per_page=5)
        
        next_url = url_for('admin.category_list', page=categories.next_num) \
            if categories.has_next else None
            
        prev_url = url_for('admin.category_list', page=categories.prev_num) \
            if categories.has_prev else None
            
        return render_template('admin-categories.html', title="Super Admin Dashboard", categories=categories, prev_url=prev_url, next_url=next_url)

    logging.warn(request.__dict__)
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})


@admin.route("/add-new/category", methods=['POST', 'GET'])
def add_category():
    admin_username = 'admin'
    admin_password = 'admin'

    if request.authorization and (request.authorization.username == admin_username and request.authorization.password == admin_password):
        if request.method == "POST":
            category_name = request.form['name'].lower()
            
            category = Categories.query.filter_by(name=category_name.capitalize()).first()
            
            if category:
                flash('That Category Name is taken!')
                return redirect(url_for('admin.add_category'))
            
            new_category = Categories(name=category_name.capitalize())
            db.session.add(new_category)
            db.session.commit()
            
            flash('New Category Added!')
            return redirect(url_for('admin.category_list'))
        return render_template('add-category.html', title="Super Admin Dashboard")

    logging.warn(request.__dict__)
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})



@admin.route("/edit-category/<category_id>", methods=['POST', 'GET'])
def edit_category(category_id):
    admin_username = 'admin'
    admin_password = 'admin'

    if request.authorization and (request.authorization.username == admin_username and request.authorization.password == admin_password):
        category = Categories.filter_by(id=category_id).first()
        
        if request.method == "POST":
            category_name = request.form['name'].lower()
            category_id = request.form['id']
            
            #search for the category name, if the id isn't the same as this, refuse itttt
            
            exisiting = Categories.query.filter_by(name=category_name.capitalize()).first()
            if exisiting.id != category_id:
                flash('This Category Name already exists!')
                return redirect(url_for('admin.edit_category', category_id=category_id))
            
            category.name = category_name.capitalize()
            db.session.commit()
            
            flash('Category Updated')
            return redirect(url_for('admin.category_list'))
        
        return render_template('edit-category.html', title="Super Admin Dashboard", category=category)

    logging.warn(request.__dict__)
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})



@admin.route("/delete-category/<category_id>", methods=['POST', 'GET'])
def delete_category(category_id):
    admin_username = 'admin'
    admin_password = 'admin'

    if request.authorization and (request.authorization.username == admin_username and request.authorization.password == admin_password):
        cateogry = Categories.query.filter_by(id=category_id).first()
        
        if category:
            db.session.delete(category)
            db.session.commit()
            flash('Category Deleted')
            
        else:
            flash('That Category does not exist!')
            
        return redirect(url_for('admin.category_list'))
        

    logging.warn(request.__dict__)
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})




@admin.route("/add/new-student", methods=['POST', 'GET'])
def create_student():
    admin_username = 'admin'
    admin_password = 'admin'

    if request.authorization and (request.authorization.username == admin_username and request.authorization.password == admin_password):
        if request.method == 'POST':
            name = request.form['name']
            username = request.form['username'].lower()
            email = request.form['email']
            index_number = request.form['indexnumber']
            group_id = request.form['groupid']
            raw_password = request.form['password']
            college = request.form['college']
            program = request.form['programme']
            group_leader = request.form['groupleader']
            staff_id = request.form['staffid']
            
            #validation
            student_check = Students.query.filter_by(username=username.capitalize()).first()
            lecturer_check = Lecturers.query.filter_by(username=username.capitalize()).first()
            
            if student_check or lecturer_check:
                flash('This Username is not available!', 'warning')
                return redirect(url_for('admin.create_student'))
            
            student_email = Students.query.filter_by(email=email).first()
            lecturer_email = Lecturers.query.filter_by(email=email).first()
            
            if student_email or lecturer_email:
                flash('This Email is taken!', 'warning')
                return redirect(url_for('admin.create_student'))
            
            lecturer_confirm = Lecturers.query.filter_by(staff_id=staff_id).first()
            if not lecturer_confirm:
                flash('That Staff ID does not exist', 'warning')
                return redirect(url_for('admin.create_student'))
            
            
            #groups validation
            # search through students, if that group_id exists, check if that student's supervisor is the same
            validate_supervisor = Students.query.filter_by(group_id=group_id).first()
            
            if validate_supervisor and validate_supervisor.staff_id != staff_id:
                flash('That is not the assigned supervisor for this group!', 'warning')
                return redirect(url_for('admin.create_student'))
            
            validate_leader = Students.query.filter_by(group_id=group_id, group_leader=True).first()
            
            if group_leader == '1' and validate_leader:
                flash('That group already has a leader!', 'warning')
                return redirect(url_for('admin.create_student'))
            
            
            index_check = Students.query.filter_by(index_number=index_number).first()
            if index_check:
                flash('That Index Number is unavailable!')
                return redirect(url_for('admin.create_student'))
            
            #hash the password
            password = bcrypt.generate_password_hash(raw_password).decode('utf-8')
            
            if group_leader == "1":
                new_student = Students(id=str(uuid.uuid4())[:8], username=username.capitalize(), name=name, email=email, password=password, index_number=index_number,
                                  program=program, group_id=group_id, college=college,supervisor=staff_id, group_leader=True)
            else:
                new_student = Students(id=str(uuid.uuid4())[:8], username=username.capitalize(), name=name, email=email, password=password,supervisor=staff_id, index_number=index_number,
                                  program=program, group_id=group_id, college=college)
            
            db.session.add(new_student)
            
            try:
                db.session.commit()
                flash('New Student Added!', 'success')
                return redirect(url_for('admin.dashboard'))
            except:
                flash('Something went wrong! Try again', 'warning')
            
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
            username = request.form['username'].lowercase()
            email = request.form['email']
            index_number = request.form['indexnumber']
            group_id = request.form['groupid']
            raw_password = request.form['password']
            college = request.form['college']
            program = request.form['programme']
            group_leader = request.form['groupleader']
            staff_id = request.form['staffid']
            
            
            #hash the password
            password = bcrypt.generate_password_hash(raw_password).decode('utf-8')
            
            student.name = name
            student.username = username.capitalize()
            student.email = email
            student.index_number = index_number
            student.group_id = group_id
            student.password = password
            student.program = program
            student.college = college
            student.supervisor = staff_id
            
            if group_leader == "1":
                student.group_leader = True
            else:
                student.group_leader = False
            
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
            username = request.form['username'].lower()
            email = request.form['email']
            staff_id = request.form['staffid']
            raw_password = request.form['password']
            college = request.form['college']
            hod = request.form['hod']
            department = request.form['department']
            
            #validation
            student_check = Students.query.filter_by(username=username.capitalize()).first()
            lecturer_check = Lecturers.query.filter_by(username=username.capitalize()).first()
            
            if student_check or lecturer_check:
                flash('This Username is not available!', 'warning')
                return redirect(url_for('admin.create_lecturer'))
            
            student_email = Students.query.filter_by(email=email).first()
            lecturer_email = Lecturers.query.filter_by(email=email).first()
            
            if student_email or lecturer_email:
                flash('This Email is taken!', 'warning')
                return redirect(url_for('admin.create_lecturer'))
            
            lecturer_confirm = Lecturers.query.filter_by(staff_id=staff_id).first()
            if lecturer_confirm:
                flash('That Staff ID has been taken!', 'warning')
                return redirect(url_for('admin.create_lecturer'))
            
            password = bcrypt.generate_password_hash(raw_password).decode('utf-8')
            
            if hod == "1":
                new_lecturer = Lecturers(id=str(uuid.uuid4())[:8], username=username.capitalize(), name=name, email=email, password=password, staff_id=staff_id,
                                  department=department,college=college, hod=True)
            else:
                new_lecturer = Lecturers(id=str(uuid.uuid4())[:8], username=username.capitalize(), name=name, email=email, password=password, staff_id=staff_id,
                                  department=department, college=college)
            
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
            username = request.form['username'].lower()
            email = request.form['email']
            staff_id = request.form['staffid']
            raw_password = request.form['password']
            college = request.form['college']
            hod = request.form['hod']
            department = request.form['department']
            
            #hash the password
            password = bcrypt.generate_password_hash(raw_password).decode('utf-8')
            
            lecturer.name = name
            lecturer.username = username.capitalize()
            lecturer.email = email
            lecturer.staff_id = staff_id
            lecturer.password = password
            lecturer.college = college
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


@admin.route("/search-results/<query>", methods=['POST', 'GET'], defaults={'page':1})
@admin.route("/search-results/<query>/<page>", methods=['POST', 'GET'])
def search_results(query, page):
    search_params = "%{}%".format(query)
    
    users = Students.query.filter(or_(Students.username == query, Students.email == query, Students.name.ilike(search_params))).paginate(page=page, per_page=5)
    
    if len(users.items) == 0:
        users = Lecturers.query.filter(or_(Lecturers.username == query, Lecturers.email == query, Lecturers.name.ilike(search_params))).paginate(page=page, per_page=5)
    
        if len(users.items) == 0:
            users = None
    
    if users:
        next_url = url_for('admin.search_results', query=query, page=users.next_num) \
            if users.has_next else None

        prev_url = url_for('admin.search_results', query=query, page=users.prev_num) \
            if users.has_prev else None
    else:
        next_url = None
        prev_url = None
    return render_template('admin-search-results.html', users=users, next_url=next_url, prev_url=prev_url)


@admin.route("/delete-user/<user_id>", methods=['POST', 'GET'])
def delete_user(user_id):
    admin_username = 'admin'
    admin_password = 'admin'

    if request.authorization and (request.authorization.username == admin_username and request.authorization.password == admin_password):
        student = Students.query.filter_by(id=user_id).first()
        lecturer = Lecturers.query.filter_by(id=user_id).first()
        if student:
            #make sure deletion is cascading for it
            flash('Student deleted successfully', 'success')
            db.session.delete(student)
            db.session.commit()
        elif lecturer:
            #make sure deletion is cascading
            flash('Lecturer deleted successfully', 'success')
            db.session.delete(lecturer)
            db.session.commit()
        else:
            flash('No User like that exists!', 'info')
            
        return redirect(url_for('admin.dashboard'))

    logging.warn(request.__dict__)
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})