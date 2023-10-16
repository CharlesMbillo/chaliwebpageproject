#chaliwebpage/urls.py
from django.urls import path
from . import views

# from .views import pdfdetails
success = views.success
urlpatterns = [
    path('userprofile/', views.UserProfile, name='UserProfile'),
    #path('userprofile_list/', views.userprofile_list, name='userprofile_list'),
    path('success/', success, name='success'),
    # path ('generate-pdf/',views.generate_pdf, name='pdf_generate'),
]
