from django.urls import path 
from accounts.views import *

app_name = "accounts"
urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("home/", HomeView.as_view(), name="home"),
    path("logout/", LogoutView.as_view(), name="logout")
]