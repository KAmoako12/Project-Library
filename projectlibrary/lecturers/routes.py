from flask import render_template, url_for, flash, redirect, Blueprint, request
from flask_login import login_user, logout_user, current_user, login_required
from projectlibrary import app, db, bcrypt
from projectlibrary.models import *


lecturers = Blueprint('lecturers', __name__)

@lecturers.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    lecturer = current_user
    students = Students.query.filter_by(supervisor=lecturer.staff_id).all()
    group_ids = []
    
    for student in students:
        group_ids.append(student.group_id)
        
    groups = set(group_ids)
    report = Reports
    return render_template('groups.html', title='Groups', lecturer=lecturer, groups=groups, report=report)


@lecturers.route('/<group_id>/abstract', methods=['GET', 'POST'])
@login_required
def abstract(group_id):
    lecturer = current_user
    report = Reports.query.filter_by(group_id=group_id).first()
    
    students = Students.query.filter_by(group_id=group_id).all()
    
    comments = Comments.query.filter_by(sender=lecturer.id, group_id=group_id).order_by(Comments.created_at.desc()).all()
    
    if request.method == 'POST':
        new_entry = request.form['comment']
        
        if new_entry.isspace() or new_entry == '':
            flash('Please enter a comment!', 'warning')
        else:
            if report:
                new_comment = Comments(group_id=group_id, report_id=report.id, comment=new_entry, sender=lecturer.id)
                flash('New Comment Added!', 'success')
                db.session.add(new_comment)
                db.session.commit()
            else:
                flash('No Reports Uploaded yet!', 'warning')
            
        return redirect(url_for('lecturers.abstract', group_id=group_id))
    return render_template('lecturer-abstract.html', lecturer=lecturer, report=report, students=students, comments=comments)


@lecturers.route('/introduction/<group_id>', methods=['GET', 'POST'])
@login_required
def report_intro(group_id):
    lecturer = current_user
    report = Reports.query.filter_by(group_id=group_id).first()
    
    intro_url = url_for('static', filename='pdfs/' + report.introduction)
    
    students = Students.query.filter_by(group_id=group_id).all()
    comments = Comments.query.filter_by(sender=lecturer.id, group_id=group_id).order_by(Comments.created_at.desc()).all()
    
    if request.method == 'POST':
        new_entry = request.form['comment']
        
        if new_entry.isspace() or new_entry == '':
            flash('Please enter a comment!', 'warning')
        else:
            if report:
                new_comment = Comments(group_id=group_id, report_id=report.id, comment=new_entry, sender=lecturer.id)
                flash('New Comment Added!', 'success')
                db.session.add(new_comment)
                db.session.commit()
            else:
                flash('No Reports Uploaded yet!', 'warning')
            
        return redirect(url_for('lecturers.abstract', group_id=group_id))
    return render_template('lecturer-introduction.html', lecturer=lecturer, report=report, intro=intro_url, students=students, comments=comments)


@lecturers.route('/literature-review/<group_id>', methods=['GET', 'POST'])
@login_required
def report_literature(group_id):
    lecturer = current_user
    report = Reports.query.filter_by(group_id=group_id).first()
    
    intro_url = url_for('static', filename='pdfs/' + report.literature_review)
    
    students = Students.query.filter_by(group_id=group_id).all()
    comments = Comments.query.filter_by(sender=lecturer.id, group_id=group_id).order_by(Comments.created_at.desc()).all()
    
    if request.method == 'POST':
        new_entry = request.form['comment']
        
        if new_entry.isspace() or new_entry == '':
            flash('Please enter a comment!', 'warning')
        else:
            if report:
                new_comment = Comments(group_id=group_id, report_id=report.id, comment=new_entry, sender=lecturer.id)
                flash('New Comment Added!', 'success')
                db.session.add(new_comment)
                db.session.commit()
            else:
                flash('No Reports Uploaded yet!', 'warning')
            
        return redirect(url_for('lecturers.abstract', group_id=group_id))
    return render_template('lecturer-introduction.html', lecturer=lecturer, report=report, intro=intro_url, students=students, comments=comments)



@lecturers.route('/methodology/<group_id>', methods=['GET', 'POST'])
@login_required
def report_methodology(group_id):
    lecturer = current_user
    report = Reports.query.filter_by(group_id=group_id).first()
    
    intro_url = url_for('static', filename='pdfs/' + report.methodology)
    
    students = Students.query.filter_by(group_id=group_id).all()
    comments = Comments.query.filter_by(sender=lecturer.id, group_id=group_id).order_by(Comments.created_at.desc()).all()
    
    if request.method == 'POST':
        new_entry = request.form['comment']
        
        if new_entry.isspace() or new_entry == '':
            flash('Please enter a comment!', 'warning')
        else:
            if report:
                new_comment = Comments(group_id=group_id, report_id=report.id, comment=new_entry, sender=lecturer.id)
                flash('New Comment Added!', 'success')
                db.session.add(new_comment)
                db.session.commit()
            else:
                flash('No Reports Uploaded yet!', 'warning')
            
        return redirect(url_for('lecturers.abstract', group_id=group_id))
    return render_template('lecturer-introduction.html', lecturer=lecturer, report=report, intro=intro_url, students=students, comments=comments)



@lecturers.route('/testing-and-evaluation/<group_id>', methods=['GET', 'POST'])
@login_required
def report_testing(group_id):
    lecturer = current_user
    report = Reports.query.filter_by(group_id=group_id).first()
    
    intro_url = url_for('static', filename='pdfs/' + report.testing_and_evaluation)
    
    students = Students.query.filter_by(group_id=group_id).all()
    comments = Comments.query.filter_by(sender=lecturer.id, group_id=group_id).order_by(Comments.created_at.desc()).all()
    
    if request.method == 'POST':
        new_entry = request.form['comment']
        
        if new_entry.isspace() or new_entry == '':
            flash('Please enter a comment!', 'warning')
        else:
            if report:
                new_comment = Comments(group_id=group_id, report_id=report.id, comment=new_entry, sender=lecturer.id)
                flash('New Comment Added!', 'success')
                db.session.add(new_comment)
                db.session.commit()
            else:
                flash('No Reports Uploaded yet!', 'warning')
            
        return redirect(url_for('lecturers.abstract', group_id=group_id))
    return render_template('lecturer-introduction.html', lecturer=lecturer, report=report, intro=intro_url, students=students, comments=comments)



@lecturers.route('/conclusion/<group_id>', methods=['GET', 'POST'])
@login_required
def report_conclusion(group_id):
    lecturer = current_user
    report = Reports.query.filter_by(group_id=group_id).first()
    
    intro_url = url_for('static', filename='pdfs/' + report.conclusion)
    
    students = Students.query.filter_by(group_id=group_id).all()
    comments = Comments.query.filter_by(sender=lecturer.id, group_id=group_id).order_by(Comments.created_at.desc()).all()
    
    if request.method == 'POST':
        new_entry = request.form['comment']
        
        if new_entry.isspace() or new_entry == '':
            flash('Please enter a comment!', 'warning')
        else:
            if report:
                new_comment = Comments(group_id=group_id, report_id=report.id, comment=new_entry, sender=lecturer.id)
                flash('New Comment Added!', 'success')
                db.session.add(new_comment)
                db.session.commit()
            else:
                flash('No Reports Uploaded yet!', 'warning')
            
        return redirect(url_for('lecturers.abstract', group_id=group_id))
    return render_template('lecturer-introduction.html', lecturer=lecturer, report=report, intro=intro_url, students=students, comments=comments)



@lecturers.route('/full-report/<group_id>', methods=['GET', 'POST'])
@login_required
def report_full(group_id):
    lecturer = current_user
    report = Reports.query.filter_by(group_id=group_id).first()
    
    intro_url = url_for('static', filename='pdfs/' + report.full_report)
    
    students = Students.query.filter_by(group_id=group_id).all()
    comments = Comments.query.filter_by(sender=lecturer.id, group_id=group_id).order_by(Comments.created_at.desc()).all()
    
    if request.method == 'POST':
        new_entry = request.form['comment']
        
        if new_entry.isspace() or new_entry == '':
            flash('Please enter a comment!', 'warning')
        else:
            if report:
                new_comment = Comments(group_id=group_id, report_id=report.id, comment=new_entry, sender=lecturer.id)
                flash('New Comment Added!', 'success')
                db.session.add(new_comment)
                db.session.commit()
            else:
                flash('No Reports Uploaded yet!', 'warning')
            
        return redirect(url_for('lecturers.abstract', group_id=group_id))
    return render_template('lecturer-introduction.html', lecturer=lecturer, report=report, intro=intro_url, students=students, comments=comments)
