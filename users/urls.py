"""Users app URL config"""

from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("signup/", views.user_signup, name="signup"),
    path("logout/", views.user_logout, name="logout"),
]