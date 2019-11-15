from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import path, include

login = Login.as_view({
    'post': 'login'
})
logout = Logout.as_view({
    'get': 'logout'
})

urlpatterns = format_suffix_patterns([
    path('o/', include('oauth2_provider.urls'), name="oauth2"),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
])
