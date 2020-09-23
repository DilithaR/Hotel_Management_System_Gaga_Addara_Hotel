from django.urls import path
from . import views

urlpatterns = [
    path("", views.method, name="method"),
]
