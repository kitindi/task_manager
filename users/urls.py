from django.urls import path 
from . import views

urlpatterns = [
    path("signup/", views.register_user, name='register-user'),
    path("", views.login_user, name='login-user'),
    path("logout/", views.logout_user, name='logout-user'),
    path("profile/", views.setup_user_profile, name='user-profile'),
    
        
    
]
