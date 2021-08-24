from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager 
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['ALPHA_SECRET_KEY'] 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.config['SERVER_NAME'] = '127.0.0.1:9000'
app.config['SECURITY_PASSWORD_SALT'] = os.environ['SECURITY_PASSWORD_SALT']
db = SQLAlchemy(app)
bcrypt = Bcrypt(app) 
login_manager = LoginManager(app)
login_manager.login_view = 'main.home'
login_manager.login_message_category = 'info'




from projectlibrary import routes
from projectlibrary.admin.routes import admin
from projectlibrary.main.routes import main
from projectlibrary.students.routes import students
#from projectlibrary.lecturers.routes import lecturers


app.register_blueprint(main)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(students, url_prefix='/student')
#app.register_blueprint(lecturers)
