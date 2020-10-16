from django.urls import path
from . import views

urlpatterns = [
    path("", views.employeeAttendence, name="employeeAttendence"), 
    path("connectCamera", views.connectCamera, name="connectCamera"),
    path("ditectEmp", views.validateEmp, name="validateEmp")
]
