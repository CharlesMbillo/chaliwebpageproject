# chaliwebpage/urls.py
from django.urls import path
from chaliwebpage import views,

#from .views import pdfdetails
urlpatterns = [
    path ('user_profile/', views.user_profile, name='user_profile'),   
    path ('success/', views.success, name='success'),
    path ('generate-pdf/',views.generate_pdf, name='pdf_generate'),
]