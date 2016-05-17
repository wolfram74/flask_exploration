import unittest
from flask.ext.testing import TestCase
from project import app, db
from project.models import User, BlogPost
from base import BaseTestCase

class FlaskTestCase(BaseTestCase):

    # def setUp(self):
    #     self.tester = app.test_client(self)
    #     self.good_cred = dict(username='admin', password='admin')
    #     self.bad_cred = dict(username='buttts', password='farts')

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

    def test_home_valid_if_authed(self):
        self.client.post(
            '/login', data=self.good_cred,
            follow_redirects= True)
        response = self.client.get('/', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)

    def test_home_protected(self):
        response = self.client.get('/', content_type = 'html/text', follow_redirects=True)
        self.assertIn('Please log in', response.data)


if __name__== '__main__':
    unittest.main()
