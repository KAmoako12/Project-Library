from projectlibrary import app
from flask import session
from datetime import timedelta


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=300)