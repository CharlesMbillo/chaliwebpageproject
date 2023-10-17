#chaliwebpage/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from .views import pdfdetails
success = views.success
#pdf = views.pdf_template
urlpatterns = [
    path('userprofile/', views.UserProfile, name='userprofile'),
    #path('pdf_template/', views.pdf, name='pdf_template'),
    path('success/', views.success, name='success'),
    # path ('generate-pdf/',views.generate_pdf, name='pdf_generate'),   

    # Login view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Logout view
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]