from django.urls import path
from . import views

urlpatterns = [
    path("account/", views.account, name="account"),
    path("logout/", views.user_logout, name="logout"),
    path("login/", views.user_login, name="login"),
]
