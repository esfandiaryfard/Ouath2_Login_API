from django.contrib.auth.models import User
from django.utils.translation import gettext as _

"""
Validate username and password 
"""


def is_vallid(username, password):
    if username is None or password is None or len(username) == 0 or len(password) == 0:
        msg = _("User and Password cannot be empty!Please enter your data")
        return msg, True

    if not User.objects.filter(username=username).exists():
        msg = _("User with this username does not exists please signup first!")
        return msg, True
