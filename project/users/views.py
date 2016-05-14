#################
#### imports ####
#################

from flask import flash, redirect, render_template, request, \
    url_for, Blueprint
from project import app
# from functools import wraps
from form import LoginForm
from project.models import User, bcrypt
from flask.ext.login import login_user, login_required, logout_user
################
#### config ####
################

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)

##########################
#### helper functions ####
##########################


# def login_required(test):
#     @wraps(test)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return test(*args, **kwargs)
#         else:
#             flash('You need to login first.')
#             return redirect(url_for('users.login'))
#     return wrap


################
#### routes ####
################

# route for handling the login page logic
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    def valid(user, password):
        exists = user is not None
        if exists:
            correct = bcrypt.check_password_hash(user.password, password)
        return exists and correct
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if valid(user, request.form['password']):
                # session['logged_in'] = True
                flash('log in successful')
                login_user(user)
                return redirect(url_for('home.home'))
            else:
                error = 'Invalid credentials. Please try again.'
        else:
            render_template('login.html', error=error, form=form)
    return render_template('login.html', error=error, form=form)


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    # session.pop('logged_in', None)
    flash('log out successful.')
    return redirect(url_for('home.welcome'))
