from flask import render_template, url_for, flash, redirect, Blueprint, request
from flask_login import login_user, logout_user, current_user, login_required
from projectlibrary import app, db, bcrypt
from projectlibrary.models import *
from  sqlalchemy.sql.expression import func



main = Blueprint('main', __name__)


@main.context_processor
def inject_user():
    user = current_user
    student = None
    lecturer = None
    categories = Categories.query.limit(6).all()
    if user.is_authenticated:
        student = Students.query.filter_by(id=user.id).first()
        lecturer = Lecturers.query.filter_by(id=user.id).first()
        
        
    return dict(student=student, lecturer=lecturer, categories=categories)


@main.route("/", methods=['POST', 'GET'], defaults={'page':1})
@main.route("/home/<int:page>", methods=['GET', 'POST'])
def home(page):
    #taking care of the reports
    reports = Reports.query.filter_by(published=True).paginate(page=page, per_page=4)
    recents = Reports.query.filter_by(published=True).order_by(Reports.updated_at.desc()).limit(5).all()
    report_len = Reports
    
    carousels = Reports.query.filter_by(published=True).order_by(func.random()).limit(5).all()
    
    
    next_url = url_for('main.home', page=reports.next_num) \
        if reports.has_next else None
        
    prev_url = url_for('main.home', page=reports.prev_num) \
        if reports.has_prev else None
            
        
    if request.method == 'POST':
        username = request.form['uname'].lower()
        password = request.form['psw'].lower()
        
        student = Students.query.filter_by(username=username.capitalize()).first()
        lecturer = Lecturers.query.filter_by(username=username.capitalize()).first()
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
    return render_template("Index.html", reports=reports, next_url=next_url, prev_url=prev_url, report_len=report_len, recents=recents, carousels=carousels)


@main.route("/abstract/<report_id>", methods=['GET', 'POST'])
def abstract(report_id):   
    report = Reports.query.filter_by(id=report_id).first()
    recents = Reports.query.filter_by(published=True).order_by(Reports.updated_at.desc()).limit(5).all()
    return render_template('abstract.html', title='Report Abstract', report=report, recents=recents)


@main.route("/full-post/<report_id>", methods=['GET', 'POST'])
def fullpost(report_id):    
    report = Reports.query.filter_by(id=report_id).first()
    return render_template('fullpost.html', title='Report Full Post', report=report)



@main.route("/colleges", methods=['POST', 'GET'])
def colleges():   
    return render_template('colleges.html', title='Colleges')


@main.route("/explore/topic/<topic>", methods=['POST', 'GET'], defaults={'page':1})
@main.route("/explore/topic/<topic>/<int:page>", methods=['POST', 'GET'])
def topic_explore(topic, page):
     #taking care of the reports
    reports = Reports.query.filter_by(published=True, topic=topic).paginate(page=page, per_page=4)
    recents = Reports.query.filter_by(published=True).order_by(Reports.updated_at.desc()).limit(5).all()
    report_len = Reports
    
    next_url = url_for('main.topic_explore', page=reports.next_num) \
        if reports.has_next else None
        
    prev_url = url_for('main.topic_explore', page=reports.prev_num) \
        if reports.has_prev else None
        
    return render_template('topic-explore.html', title=topic, reports=reports, prev_url=prev_url, next_url=next_url, report_len=report_len, recents=recents)


@main.route("/explore/college/<college>", methods=['POST', 'GET'], defaults={'page':1})
@main.route("/explore/college/<college>/<int:page>", methods=['POST', 'GET'])
def college_explore(college, page):
     #taking care of the reports
    reports = Reports.query.filter_by(published=True, college=college).paginate(page=page, per_page=4)
    recents = Reports.query.filter_by(published=True).order_by(Reports.updated_at.desc()).limit(5).all()
    report_len = Reports
    
    next_url = url_for('main.college_explore', page=reports.next_num) \
        if reports.has_next else None
        
    prev_url = url_for('main.college_explore', page=reports.prev_num) \
        if reports.has_prev else None
        
    return render_template('college-explore.html', title=college, reports=reports, prev_url=prev_url, next_url=next_url, report_len=report_len, recents=recents)


@main.route('/search/<query>', methods=['POST', 'GET'], defaults={'page':1})
@main.route('/search/<query>/<int:page>', methods=['POST', 'GET'])
def search(query, page):
    search_params = "%{}%".format(query)
    
    reports = Reports.query.filter(Reports.title.ilike(search_params) | Reports.abstract.ilike(search_params) | Reports.introduction.ilike(search_params) | Reports.literature_review.ilike(search_params) | Reports.methodology.ilike(search_params) | Reports.testing_and_evaluation.ilike(search_params) | Reports.conclusion.ilike(search_params)).paginate(page=page, per_page=5)
    
    
    recents = Reports.query.filter_by(published=True).order_by(Reports.updated_at.desc()).limit(5).all()
    report_len = Reports
    
    next_url = url_for('main.home', page=reports.next_num) \
        if reports.has_next else None
        
    prev_url = url_for('main.home', page=reports.prev_num) \
        if reports.has_prev else None
        
    return render_template('search-results.html', title="Search Results", reports=reports, recents=recents, report_len=report_len, next_url=next_url, prev_url=prev_url, query=query)


@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))