from django.urls import path
from . import views

urlpatterns = [
    path("", views.revokedPayment, name="revokedPayment"),
]