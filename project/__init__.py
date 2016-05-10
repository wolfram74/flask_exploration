#################
#### imports ####
#################

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
import os

################
#### config ####
################

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from project.users.views import users_blueprint
from project.home.views import home_blueprint

# register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)
