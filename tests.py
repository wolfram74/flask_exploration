from project import app
import unittest

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.tester = app.test_client(self)
        self.good_cred = dict(username='admin', password='admin')
        self.bad_cred = dict(username='buttts', password='farts')

    def test_index(self):
        response = self.tester.get('/login', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_message(self):
        response = self.tester.get('/login', content_type = 'html/text')
        self.assertIn(b'Please login', response.data)

    def test_login_good_auth(self):
        response = self.tester.post(
            '/login', data=self.good_cred,
            follow_redirects= True)
        self.assertIn(b'log in successful', response.data)
        self.assertEqual(response.status_code, 200)

    def test_login_bad_auth(self):
        response = self.tester.post('/login', data=self.bad_cred, follow_redirects= True)
        self.assertIn(b'Invalid credentials', response.data)
        self.assertEqual(response.status_code, 200)

    def test_logout_valid(self):
        self.tester.post(
            '/login', data=self.good_cred,
            follow_redirects= True)
        response = self.tester.get('/logout', content_type = 'html/text',follow_redirects= True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('successful', response.data)

    def test_logout_protected(self):
        response = self.tester.get('/logout', content_type = 'html/text',follow_redirects= True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('need to login', response.data)

    def test_welcome_valid(self):
        response = self.tester.get('/welcome', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)

    def test_home_valid_if_authed(self):
        self.tester.post(
            '/login', data=self.good_cred,
            follow_redirects= True)
        response = self.tester.get('/', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)

    def test_home_contains_content(self):
        self.tester.post(
            '/login', data=self.good_cred,
            follow_redirects= True)
        response = self.tester.get('/', content_type = 'html/text')
        self.assertIn('Posts', response.data)

    def test_home_protected(self):
        response = self.tester.get('/', content_type = 'html/text', follow_redirects=True)
        self.assertIn('need to login', response.data)


if __name__== '__main__':
    unittest.main()
