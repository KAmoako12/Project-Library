from flask import render_template, url_for, flash, redirect, Blueprint, request
from flask_login import login_user, logout_user, current_user, login_required
from projectlibrary import app, db, bcrypt
from projectlibrary.models import *


students = Blueprint('students', __name__)


@students.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    student = current_user
    return render_template('dashboard.html', title='Student Dashboard', student=student)