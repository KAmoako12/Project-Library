from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager 
from flask_mail import Mail
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'testing-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#app.config['SERVER_NAME'] = 'localhost:9000'
app.config['SECURITY_PASSWORD_SALT'] = 'lalala'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app) 
login_manager = LoginManager(app)
login_manager.login_view = 'main.home'
login_manager.login_message_category = 'info'



#mail extensions
app.config['MAIL_SERVER'] = 'smtp.gmail.com'      # using google's mail service
app.config['MAIL_PORT'] = 465 # well this is the mail port
app.config['MAIL_USE_TL'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'projectlibraryyy@gmail.com'
app.config['MAIL_PASSWORD'] = 'Library2021'
mail = Mail(app) # instance of the mail app


from projectlibrary import routes
from projectlibrary.admin.routes import admin
from projectlibrary.main.routes import main
from projectlibrary.students.routes import students
from projectlibrary.lecturers.routes import lecturers


app.register_blueprint(main)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(students, url_prefix='/student')
app.register_blueprint(lecturers)
