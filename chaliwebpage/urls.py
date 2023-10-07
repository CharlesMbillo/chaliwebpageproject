# chaliwebpage/urls.py
from django.urls import path, reverse
from . import views
#from .views import pdfdetail

url = reverse('user_profile')
urlpatterns = [
    path ('user_profile/', views.user_profile, name='user_profile'),
    path ('success/', views.success, name='success'),
]


