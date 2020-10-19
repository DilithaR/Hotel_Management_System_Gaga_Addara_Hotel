from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.employeeAttendence, name="employeeAttendence"), 
    path("connectCamera", views.connectCamera, name="connectCamera"),
    path("ditectEmp", views.validateEmp, name="validateEmp"), 
    path("markAttendence", views.markAttendence, name="markAttendence"),
    path("login/", include('userlogin.urls'))
]
