from django.urls import path
from . import views


urlpatterns = [
    path("", views.home , name="home"),
    path("login", views.login, name="login"),
    path("vertifyLogin", views.vertifyLogin, name="vertifyLogin"),
    path("signUp", views.signUp , name="signUp"),
    path("admin", views.admin, name="admin"), 
    path("signUpVer", views.signUpVer, name="signUpVer"),
    path("myprofile", views.myprofile, name="myprofile"),
    path("updateCus/<int:id_cus>", views.updateCus, name="updateCus"),
    path("forgetpassword", views.forgetpassword, name="forgetpassword"),
    path("forgetpw2", views.forgetpw2, name="forgetpw2"),
    path("fogetPw3", views.fogetPw3, name="fogetPw3"),
    path("customerLogout", views.customerLogout, name="customerLogout"),
    path("addEmployees", views.addEmployees, name="addEmployees"),
    path("adduser", views.adduser, name="adduser"),
    path("fullemployee/<int:id_emp>", views.fullemployee, name="fullemployee"),
    path("fullemployee/editemp", views.editemp, name="editemp"),
    path("fullemployee/employeerepo", views.employeerepo, name="employeerepo"),
    path("employeeList", views.employeeList, name="employeeList"),
    path("filterEmployees", views.filterEmployees , name="filterEmployees"),
    
]
