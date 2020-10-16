from django.urls import path
from . import views

urlpatterns = [
    path("method/cashPayment", views.cashPayment, name="cashPayment")
]
