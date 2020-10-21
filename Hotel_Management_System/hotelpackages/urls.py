from django.urls import path
from . import views


urlpatterns = [
    path('viewbooking', views.viewbooking, name='viewbooking'),
    path('booking', views.booking, name='booking'),
    path('packages', views.packages, name='packages'),
    path('viewpackages', views.viewpackages, name='viewpackages'),
    path('modifypackages', views.modifypackages, name='modifypackages'),
    path('offers', views.offers, name='offers'),
    path('packages_home', views.packages_home, name='packages_home'),

    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]
