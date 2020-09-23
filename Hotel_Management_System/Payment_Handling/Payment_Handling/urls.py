from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('method.urls')),
    path('admin/', admin.site.urls),
    path('cashPayment/', include('cashPayment.urls')),
    path('cardPayment/', include('cardPayment.urls')),
    path('cashDashboard/', include('cashDashboard.urls')),
    path('cardDashboard/', include('cardDashboard.urls')),
    path('paymentReport/', include('paymentReport.urls')),
    path('revokedPayment/', include('revokedPayment.urls')),
    path('removePayment/', include('removePayment.urls')),
]
