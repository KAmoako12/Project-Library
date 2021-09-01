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
    page_title = "Abstract"
    lecturer = current_user
    report = Reports.query.filter_by(group_id=group_id).first()
    page_text = report.abstract
    
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
    return render_template('lecturer-abstract.html', lecturer=lecturer, report=report, students=students, comments=comments, page_text=page_text, page_title=page_title)


@lecturers.route('/introduction/<group_id>', methods=['GET', 'POST'])
@login_required
def report_intro(group_id):
    page_title = "Introduction"
    lecturer = current_user
    report = Reports.query.filter_by(group_id=group_id).first()
    
    page_text = report.introduction
    
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
            
        return redirect(url_for('lecturers.report_intro', group_id=group_id))
    return render_template('lecturer-abstract.html',page_title=page_title, lecturer=lecturer, report=report, page_text=page_text, students=students, comments=comments)


@lecturers.route('/literature-review/<group_id>', methods=['GET', 'POST'])
@login_required
def report_literature(group_id):
    page_title = "Literature Review"
    lecturer = current_user
    report = Reports.query.filter_by(group_id=group_id).first()
    
    page_text =  report.literature_review
    
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
            
        return redirect(url_for('lecturers.report_literature', group_id=group_id))
    return render_template('lecturer-abstract.html', page_title=page_title, lecturer=lecturer, report=report, page_text=page_text, students=students, comments=comments)



@lecturers.route('/methodology/<group_id>', methods=['GET', 'POST'])
@login_required
def report_methodology(group_id):
    page_title = "Methodology"
    lecturer = current_user
    report = Reports.query.filter_by(group_id=group_id).first()
    
    page_text =  report.methodology
    
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
            
        return redirect(url_for('lecturers.report_methodology', group_id=group_id))
    return render_template('lecturer-abstract.html', page_title=page_title, lecturer=lecturer, report=report, page_text=page_text, students=students, comments=comments)



@lecturers.route('/testing-and-evaluation/<group_id>', methods=['GET', 'POST'])
@login_required
def report_testing(group_id):
    page_title = "Testing and Evaluation"
    lecturer = current_user
    report = Reports.query.filter_by(group_id=group_id).first()
    
    page_text =  report.testing_and_evaluation
    
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
            
        return redirect(url_for('lecturers.report_testing', group_id=group_id))
    return render_template('lecturer-abstract.html', page_title=page_title, lecturer=lecturer, report=report, page_text=page_text, students=students, comments=comments)



@lecturers.route('/conclusion/<group_id>', methods=['GET', 'POST'])
@login_required
def report_conclusion(group_id):
    page_title = "Conclusion"
    lecturer = current_user
    report = Reports.query.filter_by(group_id=group_id).first()
    
    page_text =  report.conclusion
    
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
            
        return redirect(url_for('lecturers.report_conclusion', group_id=group_id))
    return render_template('lecturer-abstract.html', page_title=page_title, lecturer=lecturer, report=report, page_text=page_text, students=students, comments=comments)



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
            
        return redirect(url_for('lecturers.report_full', group_id=group_id))
    return render_template('lecturer-introduction.html', lecturer=lecturer, report=report, intro=intro_url, students=students, comments=comments)



@lecturers.route('/<group_id>/delete-comment/<comment_id>', methods=['GET', 'POST'])
@login_required
def delete_comment(group_id, comment_id):
    comment = Comments.query.filter_by(id=comment_id).first()
    
    if comment:
        db.session.delete(comment)
        db.session.commit()
        flash('Comment Deleted')
        return redirect(url_for('lecturers.abstract', group_id=group_id))


@lecturers.route('/publish-report/<report_id>', methods=['GET', 'POST'])
@login_required
def publish_report(report_id):
    report = Reports.query.filter_by(id=report_id).first()
    
    lecturer = current_user
    if lecturer.staff_id == report.supervisor or lecturer.hod:
        if report.full_report:
            report.published = True
            db.session.commit()
            flash('The report has been published successfully!', 'success')
            
        else:
            flash('The full report needs to be published first!', 'warning')
    else:
        flash('Only Supervisors or HODS can publish the reports!', 'warning')
        
    return redirect(url_for('lecturers.abstract', group_id=report.group_id))


@lecturers.route('/unpublish-report/<report_id>', methods=['GET', 'POST'])
@login_required
def unpublish_report(report_id):
    report = Reports.query.filter_by(id=report_id).first()
    
    lecturer = current_user
    if lecturer.staff_id == report.supervisor or lecturer.hod:
        if report.published:
            report.published = False
            db.session.commit()
            flash('The report has been removed from publishment successfully!', 'success')
            
        else:
            flash('The full report needs to be published first!', 'warning')
    else:
        flash('Only Supervisors or HODS can unpublish the reports!', 'warning')
        
    return redirect(url_for('lecturers.abstract', group_id=report.group_id))
