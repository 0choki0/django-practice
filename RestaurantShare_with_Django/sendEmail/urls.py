from django.urls import path, include
from . import views

app_name = 'sendEmail'

urlpatterns =[
    path('send/', views.sendEmail)
]