from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path("", views.cardDashboard, name="cardDashboard"),
    url(r'^delete_card/(?P<id>\d+)$', views.delete_card, name="delete_card")
]