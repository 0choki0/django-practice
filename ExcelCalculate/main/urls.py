from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('verifyCode', views.verifyCode, name='verifyCode'),
    path('verify', views.verify, name='verify'),
    path('result', views.result, name='result'),
]