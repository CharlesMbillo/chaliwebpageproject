# chaliwebpage/urls.py
from django.urls import path, reverse
from . import views

#from .views import pdfdetails
urlpatterns = [
    path ('user_profile/', views.user_profile, name='user_profile'),   
    path ('success/', views.success, name='success'),
]