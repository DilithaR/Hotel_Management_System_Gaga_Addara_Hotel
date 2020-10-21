from django.urls import path
from . import views
from food_home import views
from cart import views as OrderViews

path("", views.homepage, name='homepage'),
