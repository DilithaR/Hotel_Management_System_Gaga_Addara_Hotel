from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.method, name="method"),
    path("cashPayment/", include('cashPayment.urls'), name="cashPayment"),
    path("cardPayment/", include('cardPayment.urls'), name="cardPayment"),
]
