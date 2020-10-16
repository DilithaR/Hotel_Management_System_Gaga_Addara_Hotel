from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path("", views.cashDashboard, name="cashDashboard"),
    url(r'^delete_cash/(?P<id>\d+)$', views.delete_cash, name="delete_cash")
]