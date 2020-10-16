from django.urls import path
from . import views

urlpatterns = [
    path("method/cardPayment", views.cardPayment, name="cardPayment")
]
