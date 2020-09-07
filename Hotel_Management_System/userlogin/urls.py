from django.urls import path
from . import views


urlpatterns = [
    path("", views.home , name="home"),
    path("login", views.login, name="login"),
    path("vertifyLogin", views.vertifyLogin, name="vertifyLogin"),
    # path("signUp", views.signUp , name="signUp")
]
