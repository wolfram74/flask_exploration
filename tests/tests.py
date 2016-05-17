import unittest
from flask.ext.testing import TestCase
from project import app, db
from project.models import User, BlogPost
from flask.ext.login import current_user

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        # self.tester = app.test_client(self)
        self.good_cred = dict(username='admin', password='admin')
        self.bad_cred = dict(username='buttts', password='farts')
        db.create_all()
        db.session.add(BlogPost('Test post', 'This is a test. Only a test.'))
        db.session.add(User('admin', 'ad@min.com', 'admin'))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        pass

class FlaskTestCase(BaseTestCase):

    def test_index(self):
        response = self.client.get('/login', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_message(self):
        response = self.client.get('/login', content_type = 'html/text')
        self.assertIn(b'Please login', response.data)

    def test_login_good_auth(self):
        response = self.client.post(
            '/login', data=self.good_cred,
            follow_redirects= True)
        self.assertIn(b'log in successful', response.data)
        self.assertEqual(response.status_code, 200)

    def test_login_bad_auth(self):
        response = self.client.post('/login', data=self.bad_cred, follow_redirects= True)
        self.assertIn(b'Invalid credentials', response.data)
        self.assertEqual(response.status_code, 200)

    def test_logout_valid(self):
        self.client.post(
            '/login', data=self.good_cred,
            follow_redirects= True)
        response = self.client.get('/logout', content_type = 'html/text',follow_redirects= True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('successful', response.data)

    def test_logout_protected(self):
        response = self.client.get('/logout', content_type = 'html/text',follow_redirects= True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Please log in', response.data)

    def test_welcome_valid(self):
        response = self.client.get('/welcome', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)

    def test_home_valid_if_authed(self):
        self.client.post(
            '/login', data=self.good_cred,
            follow_redirects= True)
        response = self.client.get('/', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)

    def test_home_contains_content(self):
        self.client.post(
            '/login', data=self.good_cred,
            follow_redirects= True)
        response = self.client.get('/', content_type = 'html/text')
        self.assertIn('Posts', response.data)

    def test_home_protected(self):
        response = self.client.get('/', content_type = 'html/text', follow_redirects=True)
        self.assertIn('Please log in', response.data)

    def test_registration(self):
        with self.client:
            response = self.client.post(
                '/register/',
                data=dict(
                    username="adam", email='test@place.com',
                    password="dupers", confirm="dupers"),
                follow_redirects=True
            )
            self.assertIn(b'Posts', response.data)
            self.assertTrue(current_user.name == "adam")
            self.assertTrue(current_user.is_active())

if __name__== '__main__':
    unittest.main()
