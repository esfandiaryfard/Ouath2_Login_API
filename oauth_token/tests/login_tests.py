from django.test import TestCase


class LoginTestCase(TestCase):
    fixtures = ['default_login']

    def test_user_can_login(self):
        response = self.client.post('/api/v1/login', data={'username': 'admin', 'password': '123'})
        self.assertEqual(response.status_code, 200)

    def test_empty_input(self):
        response = self.client.post('/api/v1/login', data={'username': '', 'password': ''})
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/api/v1/login', data={'username': '', 'password': '123456789'})
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/api/v1/login', data={'username': 'admin', 'password': ''})
        self.assertEqual(response.status_code, 400)

    def test_wrong_input(self):
        response = self.client.post('/api/v1/login', data={'username': 'adm', 'password': '123'})
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/api/v1/login', data={'username': 'admin', 'password': '123123'})
        self.assertEqual(response.status_code, 400)

