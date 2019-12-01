# Ouath2_Login_API
This project is a simple login/logout API using oauth2 Grant Type: Resource Owner Password Credentials
for knowing more about oauth2 read: https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2
in this project I am using django oauth toolkit https://django-oauth-toolkit.readthedocs.io/en/latest/

After you get this project, install the packages and migrate to create database, you need to create oauth client using this command:
  from oauth2_provider.models import Application
  Application.objects.create(authorization_grant_type=Application.GRANT_PASSWORD, client_type=Application.CLIENT_CONFIDENTIAL)
  
Then you need to create a config file like example and add client_id and client_secret there.You need also add your server data in config file.

Now your previously created superuser or user can get the token for access protected api using /login endpoint
