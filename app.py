from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
import os
# import sqlite3

app = Flask(__name__)
app.database = 'sample.db'
app.config.from_object(os.environ['APP_SETTINGS'])
print os.environ['APP_SETTINGS']
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from models import *

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    # try:
    #     g.db = connect_db()
    #     cur = BlogPost.query.all()
    #     posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    # except:
    #     flash('database error')
    #     posts=[]
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('log in successful')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('logout successful')
    return redirect(url_for('welcome'))

# def connect_db():
#     return sqlite3.connect(app.database)

if __name__ == '__main__':
    app.run()
