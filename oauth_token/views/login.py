import datetime

import requests
from django.utils.translation import gettext as _
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from login.config import *
from oauth_token.validations import *

"""
Get Username and password from user and add client_id and client_Secret and grant_type,then send it to token 
endpoint and show the token in output.
"""


class Login(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def login(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')

            not_valid = login.is_vallid(username, password)

            if not_valid:
                msg = not_valid[0]
                return Response({"message": msg}, status=status.HTTP_400_BAD_REQUEST)

            data = {'grant_type': 'password',
                    'client_id': os.environ.get("client_id"),
                    'client_secret': os.environ.get("client_secret"),
                    'username': username,
                    'password': password}

            token = requests.post(os.environ['token_login'], data=data)

            if token.status_code == 200:
                User.objects.filter(username=username).update(last_login=datetime.datetime.now())

                return Response(token.json())

            if token.status_code == 400:
                return Response({"message": _("Password is not valid.Please check your password!")},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message": _("Something is wrong with the server!Please call administrators!")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            return Response({"message": _("Something is wrong with the server!Please call administrators!")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
