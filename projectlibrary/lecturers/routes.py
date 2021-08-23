from flask import render_template, url_for, flash, redirect, Blueprint, request
from flask_login import login_user, logout_user, current_user, login_required
from projectlibrary import app, db, bcrypt
from projectlibrary.models import *


lecturers = Blueprint('lecturers', __name__)

@lecutrers.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    lecturer = current_user
    return lecturer.username