
from django.urls import path
from .views import *

app_name = 'cl'
# 기본주소 : 127.0.0.1:8000/cl/
urlpatterns = [
    # 127.0.0.1:8000/cl/signup/
    path('signup/', signup, name = 'signup'),
    # 127.0.0.1:8000/cl/signin/
    path('signin/', signin, name = "signin"),
    # 127.0.0.1:8000/cl/signout/
    path('signout/', signout, name = 'signout')
    ]