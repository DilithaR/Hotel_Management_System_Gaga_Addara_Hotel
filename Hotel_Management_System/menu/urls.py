from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:food>/', views.customize, name='customize'),
    path('menuBackCreate', views.menuBackCreate, name='menuBackCreate'),
    path('menuBackUpdate/<str:pk>/', views.menuBackUpdate, name='menuBackUpdate'),
    path('menuBackDelete/<str:pk>/', views.menuBackDelete, name='menuBackDelete'),
    path('promoBackCreate', views.promoBackCreate, name='promoBackCreate'),
    path('promoBackUpdate/<str:pk>/', views.promoBackUpdate, name='promoBackUpdate'),
    path('promoBackDelete/<str:pk>/', views.promoBackDelete, name='promoBackDelete'),
    path('deletefromcartback/<int:id>', views.deletefromcartback, name='deletefromcartback'),
    path('getPdfPage', views.getPdfPage, name='getPdfPage'),
]
