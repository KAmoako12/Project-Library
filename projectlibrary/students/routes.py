from flask import render_template, url_for, flash, redirect, Blueprint, request
from flask_login import login_user, logout_user, current_user, login_required
from projectlibrary import app, db, bcrypt
from projectlibrary.models import *
from projectlibrary.misc import *


students = Blueprint('students', __name__)


@students.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    page_title = "Abstract"
    student = current_user
    report = Reports.query.filter_by(group_id=student.group_id).first()
    
    page_text = None
    
    comments = Comments.query.filter_by(group_id=student.group_id).order_by(Comments.created_at.desc()).all()
    lecturer = Lecturers.query.filter_by(staff_id=student.supervisor).first()
    
    if report:
        page_text = report.abstract
    
    if request.method == 'POST':
        abstract = request.form['page_text']
        if abstract.isspace() or abstract=='':
            flash('Kindly Enter an abstract', 'warning')
        else:
            if report:
                report.abstract = abstract
                flash('Abstract Updated', 'success')
                db.session.commit()
            else:
                flash('You need to upload report details first!', 'warning')
            
        return redirect(url_for('students.dashboard'))
    
    return render_template('dashboard.html', page_title=page_title, student=student, report=report, comments=comments, lecturer=lecturer, page_text=page_text)


@students.route('/introduction', methods=['GET', 'POST'])
@login_required
def report_intro():
    page_title = "Introduction"
    student = current_user
    report = Reports.query.filter_by(group_id=student.group_id).first()
    
    page_text = None
    
    comments = Comments.query.filter_by(group_id=student.group_id).order_by(Comments.created_at.desc()).all()
    lecturer = Lecturers.query.filter_by(staff_id=student.supervisor).first()
    
    if report:
        page_text = report.introduction
    
    if request.method == 'POST':
        text = request.form['page_text']
        if text.isspace() or text=='':
            flash('Kindly enter some text!', 'warning')
        else:
            if report:
                report.introduction = text
                flash('Introduction Updated', 'success')
                db.session.commit()
            else:
                flash('You need to upload report details first!', 'warning')
            
        return redirect(url_for('students.report_intro'))
    
    return render_template('dashboard.html', page_title=page_title, student=student, report=report, comments=comments, lecturer=lecturer, page_text=page_text)


@students.route('/literature-review', methods=['GET', 'POST'])
@login_required
def report_literature():
    page_title = "Literature Review"
    student = current_user
    report = Reports.query.filter_by(group_id=student.group_id).first()
    page_text = None
    
    comments = Comments.query.filter_by(group_id=student.group_id).order_by(Comments.created_at.desc()).all()
    lecturer = Lecturers.query.filter_by(staff_id=student.supervisor).first()
    
    if report:
        page_text = report.literature_review
    
    if request.method == 'POST':
        text = request.form['page_text']
        if text.isspace() or text=='':
            flash('Kindly enter some text!', 'warning')
        else:
            if report:
                report.literature_review = text
                flash('Literature Review Updated', 'success')
                db.session.commit()
            else:
                flash('You need to upload report details first!', 'warning')
            
        return redirect(url_for('students.report_literature'))
    
    return render_template('dashboard.html', page_title=page_title, student=student, report=report, page_text=page_text, comments=comments, lecturer=lecturer)


@students.route('/methodology', methods=['GET', 'POST'])
@login_required
def report_methodology():
    page_title = "Methodology"
    student = current_user
    report = Reports.query.filter_by(group_id=student.group_id).first()
    page_text = None
    
    comments = Comments.query.filter_by(group_id=student.group_id).order_by(Comments.created_at.desc()).all()
    lecturer = Lecturers.query.filter_by(staff_id=student.supervisor).first()
    
    if report:
        page_text = report.methodology
    
    if request.method == 'POST':
        text = request.form['page_text']
        if text.isspace() or text=='':
            flash('Kindly enter some text!', 'warning')
        else:
            if report:
                report.methodology = text
                flash('Methodology Updated', 'success')
                db.session.commit()
            else:
                flash('You need to upload report details first!', 'warning')
            
        return redirect(url_for('students.report_methodology'))
    
    return render_template('dashboard.html', page_title=page_title, student=student, report=report, page_text=page_text, comments=comments, lecturer=lecturer)


@students.route('/testing-and-evaluation', methods=['GET', 'POST'])
@login_required
def report_testing():
    page_title = "Testing and Evaluation"
    student = current_user
    report = Reports.query.filter_by(group_id=student.group_id).first()
    page_text = None
    
    comments = Comments.query.filter_by(group_id=student.group_id).order_by(Comments.created_at.desc()).all()
    lecturer = Lecturers.query.filter_by(staff_id=student.supervisor).first()
    
    if report:
        page_text = report.testing_and_evaluation
    
    if request.method == 'POST':
        text = request.form['page_text']
        if text.isspace() or text=='':
            flash('Kindly enter some text!', 'warning')
        else:
            if report:
                report.testing_and_evaluation = text
                flash('Testing and Evaluation Updated', 'success')
                db.session.commit()
            else:
                flash('You need to upload report details first!', 'warning')
            
        return redirect(url_for('students.report_testing'))
    
    return render_template('dashboard.html',page_title=page_title, student=student, report=report, page_text=page_text, comments=comments, lecturer=lecturer)


@students.route('/conclusion', methods=['GET', 'POST'])
@login_required
def report_conclusion():
    page_title = "Conclusion"
    student = current_user
    report = Reports.query.filter_by(group_id=student.group_id).first()
    
    page_text = None
    
    comments = Comments.query.filter_by(group_id=student.group_id).order_by(Comments.created_at.desc()).all()
    lecturer = Lecturers.query.filter_by(staff_id=student.supervisor).first()
    
    if report:
        page_text = report.conclusion
    
    if request.method == 'POST':
        text = request.form['page_text']
        if text.isspace() or text=='':
            flash('Kindly enter some text!', 'warning')
        else:
            if report:
                report.conclusion = text
                flash('Conclusion Updated', 'success')
                db.session.commit()
            else:
                flash('You need to upload report details first!', 'warning')
            
        return redirect(url_for('students.report_conclusion'))
    
    return render_template('dashboard.html', student=student, page_title=page_title, report=report, page_text=page_text, comments=comments, lecturer=lecturer)


@students.route('/full-report', methods=['GET', 'POST'])
@login_required
def report_full():
    student = current_user
    report = Reports.query.filter_by(group_id=student.group_id).first()
    
    comments = Comments.query.filter_by(group_id=student.group_id).order_by(Comments.created_at.desc()).all()
    lecturer = Lecturers.query.filter_by(staff_id=student.supervisor).first()
    
    intro_url = url_for('static', filename='pdfs/' + report.full_report)
    
    return render_template('introduction.html', student=student, report=report, intro=intro_url, comments=comments, lecturer=lecturer)
        

@students.route('/upload-report', methods=['GET', 'POST'])
@login_required
def upload_report():
    student = current_user
    report = Reports.query.filter_by(group_id=student.group_id).first()
    categories = Categories.query.all()
    
    if request.method =='POST':
        title = request.form['title']
        group_id = request.form['groupid']
        college = request.form['college']
        topic = request.form['topic']
        file =None
        chapter = None
        
        
        if report:
            file = request.files['file']
            chapter = request.form['chapter']
            
        
        #if report exists, do this part
        if report:
            report.title = title
            report.topic = topic
            report.group_id = group_id
            report.college = college
#            report.chapter = chapter
            
            #if there's an image save it
            report.image='default.jpg'
            
            
            # depending on the chapter, save as such
            if chapter == 'introduction':
                pdf_file = save_pdf(file)
                report.introduction = pdf_file
            elif chapter == 'literature':
                pdf_file = save_pdf(file)
                report.literature_review = pdf_file
            elif chapter == 'methodology':
                pdf_file = save_pdf(file)
                report.methodology = pdf_file
            elif chapter == 'testing':
                pdf_file = save_pdf(file)
                report.testing_and_evaluation = pdf_file
            elif chapter == 'conclusion':
                pdf_file = save_pdf(file)
                report.conclusion = pdf_file
            else:
                pdf_file = save_pdf(file)
                report.full_report = pdf_file
                
            db.session.commit()
            flash('Report Updated', 'success')
            return redirect(url_for('students.dashboard'))
            
        #else, update it based on what's there
        else:
             #if there's an image save it
           
            picture_file = 'default.jpg'
            
            
            # depending on the chapter, save as such
            if chapter == 'introduction':
                pdf_file = save_pdf(file)
                new_report = Reports(topic=topic, title=title, group_id=group_id, college=college, image=picture_file,
                                    introduction=pdf_file, supervisor=student.supervisor)
                
            elif chapter == 'literature':
                pdf_file = save_pdf(file)
                new_report = Reports(topic=topic, title=title, group_id=group_id, college=college, image=picture_file,
                                    literature_review=pdf_file, supervisor=student.supervisor)
            elif chapter == 'methodology':
                pdf_file = save_pdf(file)
                new_report = Reports(topic=topic, title=title, group_id=group_id, college=college, image=picture_file,
                                    methodology=pdf_file, supervisor=student.supervisor)
                
            elif chapter == 'testing':
                pdf_file = save_pdf(file)
                new_report = Reports(topic=topic, title=title, group_id=group_id, college=college, image=picture_file,
                                    testing_and_evaluation=pdf_file, supervisor=student.supervisor)
                
            elif chapter == 'conclusion':
                pdf_file = save_pdf(file)
                new_report = Reports(topic=topic, title=title, group_id=group_id, college=college, image=picture_file,
                                    conclusion=pdf_file, supervisor=student.supervisor)
                
            else:
                if chapter == 'fullreport':
                    pdf_file = save_pdf(file)
                    new_report = Reports(topic=topic, title=title, group_id=group_id, college=college, image=picture_file,
                                        full_report=pdf_file, supervisor=student.supervisor)
                    
                else:
                    new_report = Reports(topic=topic, title=title, group_id=group_id, college=college, supervisor=student.supervisor)
                    
            db.session.add(new_report)
            db.session.commit()
            
            flash('New Report Added', 'success')
            return redirect(url_for('students.dashboard'))
        
    return render_template('upload-report.html', title='Upload Report', student=student, report=report, categories=categories)