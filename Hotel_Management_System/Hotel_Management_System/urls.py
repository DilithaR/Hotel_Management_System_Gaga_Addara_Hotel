"""Hotel_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include('userlogin.urls')),
    path("method/", include('method.urls')),

    #Sayuru URL s

    path('cashPayment/', include('cashPayment.urls')),
    path('cardPayment/', include('cardPayment.urls')),
    path('cashDashboard/', include('cashDashboard.urls')),
    path('cardDashboard/', include('cardDashboard.urls')),
    path('paymentReport/', include('paymentReport.urls')),
    path('revokedPayment/', include('revokedPayment.urls')),
    path('removePayment/', include('removePayment.urls')),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
