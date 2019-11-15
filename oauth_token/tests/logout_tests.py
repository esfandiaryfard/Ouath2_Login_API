from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIRequestFactory
from oauth2_provider.models import AccessToken, RefreshToken, Application
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from oauth_token.views import Logout


class LogoutTestCase(TestCase):
    fixtures = ['default_login']

    def setUp(self):
        response = self.client.post('/api/v1/login', data={'username': 'admin', 'password': '123'})
        Application.objects.create(authorization_grant_type=Application.GRANT_PASSWORD,
                                   client_type=Application.CLIENT_CONFIDENTIAL)
        AccessToken.objects.create(token=response.json()['access_token'],
                                   expires=timezone.now() + timezone.timedelta(seconds=response.json()['expires_in']),
                                   user_id=1, application_id=1)

    def test_user_logout(self):
        factory = APIRequestFactory()
        view = Logout.as_view({'get': 'logout'})
        request = factory.get('/api/v1/logout')
        user = User.objects.get(username='admin')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEquals(response.status_code, 200)


