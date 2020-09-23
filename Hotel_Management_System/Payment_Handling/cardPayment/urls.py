from django.urls import path
from . import views

urlpatterns = [
    path("cardPayment", views.cardPayment, name="cardPayment")
]