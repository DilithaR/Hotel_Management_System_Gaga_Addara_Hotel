from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.attendenceReport, name="attendenceReport"),
    path("generatePDf", views.generatePDf, name="generatePDf")
]
