import requests
from django.utils.translation import gettext as _
from rest_framework import status, viewsets
from rest_framework.response import Response

from login.config import *

"""For each request token gets from header and including client id and client secret a request to 
revoke_token, logout the user"""


class Logout(viewsets.ViewSet):

    def logout(self, request):
        try:
            data = {'token': request.META.get('HTTP_AUTHORIZATION', ''),
                    'client_id': os.environ.get("client_id"),
                    'client_secret': os.environ.get("client_secret")}

            result = requests.post(os.environ['token_logout'], data=data)

            if result.status_code == 200:
                return Response({"message": _("Logged out successfullt")}, status=status.HTTP_200_OK)

            else:
                return Response({"message": _("Something is wrong with the server!Please call administrators!")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            print(e)
            return Response({"message": _("Something is wrong with the server!Please call administrators!")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
