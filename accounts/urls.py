from django.urls import path
from accounts.views import loginview, logoutview, signupview

app_name = "accounts"

urlpatterns = [
    path("login", loginview, name="login"),
    path("logout", logoutview, name="logout"),
    path("signup", signupview, name="signup"),
]