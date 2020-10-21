from django.urls import path
from . import views


urlpatterns = [
    path('addrespackage', views.addrespackage),
    path('addres', views.addres),
    path('viewResPackage', views.viewpack),
    path('viewres', views.viewres),
    path('CviewResPackage', views.Cviewpack),
    path('Cviewres', views.Cviewres),
    path('viewResPackage/<int:RH_packageID>', views.delete),
    path('viewres/<int:RH_reserveID>', views.deleteres),
    path('editResPackage/<int:RH_packageID>', views.edit),
    path('update/<int:RH_packageID>', views.update),
    path('getPdfPage', views.getPdfPage, name='getPdfPage'),
]
