# chaliwebpage/urls.py
from django.urls import path
from . import views
#from .views import pdfdetail

urlpatterns = [
    path ('user_profile/', views.user_profile, name='user_profile'),
    path ('success/', views.success, name='success'),
]


