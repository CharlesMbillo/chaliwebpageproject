#chaliwebpage/urls.py
#from django.conf import urls
from django.urls import path
#from django.contrib.auth import views as auth_views
from chaliwebpage import views
# from .views import pdfdetails
success = views.success
# pdf = views.pdf_template
urlpatterns = [
    path('userprofile/', views.UserProfile, name='userprofile'),
    # path('pdf_template/', views.pdf, name='pdf_template'),
    path('success/', views.success, name='success'),
    # Login view
   # path('login/', auth_views.LoginView.as_view(login), name='login'), 
    # Logout view
    #path('logout/', auth_views.LogoutView.as_view(logout), name='logout'),
    path('create-user/', views.create_user, name='create_user')
]