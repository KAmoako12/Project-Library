from flask import render_template, url_for, flash, redirect, Blueprint, request
from flask_login import login_user, logout_user, current_user
from projectlibrary import app, db, bcrypt
from projectlibrary.models import *


main = Blueprint('main', __name__)

@main.route("/", methods=['POST', 'GET'])
@main.route("/home", methods=['POST', 'GET'])
@main.route("/index", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        print('Posted!')
        
        return redirect(url_for('main.home'))
    return render_template("Index.html")