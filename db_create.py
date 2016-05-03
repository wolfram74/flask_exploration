from app import db
from models import BlogPost, User

db.drop_all()
db.create_all()

db.session.add(BlogPost('Good', "I\'m good"))
db.session.add(BlogPost('Well', "I\'m well"))

db.session.add(User('admin', 'ad@min.com', 'admin'))

db.session.commit()

