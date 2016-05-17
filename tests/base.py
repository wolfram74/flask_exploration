from flask.ext.testing import TestCase
from project import app, db
from project.models import User, BlogPost

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        # self.tester = app.test_client(self)
        self.good_cred = dict(username='admin', password='admin')
        self.bad_cred = dict(username='buttts', password='farts')
        db.create_all()
        db.session.add(BlogPost('Test post', 'This is a test. Only a test.', 1))
        db.session.add(User('admin', 'ad@min.com', 'admin'))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        pass
