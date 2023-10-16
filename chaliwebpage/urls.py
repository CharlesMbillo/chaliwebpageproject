#chaliwebpage/urls.py
from django.urls import path
from . import views

# from .views import pdfdetails
success = views.success
urlpatterns = [
    path('user_profile/', views.user_profile, name='user_profile'),
    path('list/', views.user_list, name='user_list'),
    path('success/', success, name='success'),
    # path ('generate-pdf/',views.generate_pdf, name='pdf_generate'),
]
