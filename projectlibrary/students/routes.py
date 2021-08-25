from flask import render_template, url_for, flash, redirect, Blueprint, request
from flask_login import login_user, logout_user, current_user, login_required
from projectlibrary import app, db, bcrypt
from projectlibrary.models import *
from projectlibrary.misc import *


students = Blueprint('students', __name__)


@students.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    student = current_user
    report = Reports.query.filter_by(group_id=student.group_id).first()
    return render_template('dashboard.html', title='Student Dashboard', student=student, report=report)


@students.route('/introduction', methods=['GET', 'POST'])
@login_required
def report_intro():
    student = current_user
    report = Reports.query.filter_by(group_id=student.group_id).first()
    
    intro_url = url_for('static', filename='pdfs/' + report.introduction)
    
    return render_template('introduction.html', student=student, report=report, intro=intro_url)


@students.route('/upload-report', methods=['GET', 'POST'])
@login_required
def upload_report():
    student = current_user
    report = Reports.query.filter_by(group_id=student.group_id).first()
    
    if request.method =='POST':
        title = request.form['title']
        group_id = request.form['groupid']
        file = request.files['file']
        image = request.files['image']
        college = request.form['college']
        chapter = request.form['chapter']
        topic = request.form['topic']
        
        #if report exists, do this part
        if report:
            report.title = title
            report.topic = topic
            report.group_id = group_id
            report.college = college
            report.chapter = chapter
            
            #if there's an image save it
            if image:
                picture_file = save_picture(image)
                report.image = picture_file
            
            
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
                report.testing_and_evalutation = pdf_file
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
            if image:
                picture_file = save_picture(image)
            else:
                picture_file = 'default.jpg'
            
            
            # depending on the chapter, save as such
            if chapter == 'introduction':
                pdf_file = save_pdf(file)
                new_report = Reports(topic=topic, title=title, group_id=group_id, college=college, image=picture_file,
                                    introduction=pdf_file)
                
            elif chapter == 'literature':
                pdf_file = save_pdf(file)
                new_report = Reports(topic=topic, title=title, group_id=group_id, college=college, image=picture_file,
                                    literature_review=pdf_file)
            elif chapter == 'methodology':
                pdf_file = save_pdf(file)
                new_report = Reports(topic=topic, title=title, group_id=group_id, college=college, image=picture_file,
                                    methodology=pdf_file)
                
            elif chapter == 'testing':
                pdf_file = save_pdf(file)
                new_report = Reports(topic=topic, title=title, group_id=group_id, college=college, image=picture_file,
                                    testing_and_evaluation=pdf_file)
                
            elif chapter == 'conclusion':
                pdf_file = save_pdf(file)
                new_report = Reports(topic=topic, title=title, group_id=group_id, college=college, image=picture_file,
                                    conclusion=pdf_file)
                
            else:
                if chapter == 'fullreport':
                    pdf_file = save_pdf(file)
                    new_report = Reports(topic=topic, title=title, group_id=group_id, college=college, image=picture_file,
                                        full_report=pdf_file)
                    
            db.session.add(new_report)
            db.session.commit()
            
            flash('New Report Added', 'success')
            return redirect(url_for('students.dashboard'))
        
    return render_template('upload-report.html', title='Upload Report', student=student, report=report)