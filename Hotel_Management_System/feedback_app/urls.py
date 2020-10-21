from django.urls import path
from . import views


urlpatterns = [
    path('addfeedback', views.addfeedback),
    path('undfb', views.undfb),
    path('dashboardFB', views.undfb),
    path('undfb/<int:feedbackId>', views.delete),
    path('editfeedback/<int:feedbackId>', views.edit),
    path('update/<int:feedbackId>', views.update),
    path('undfb/<int:feedbackId>', views.update),
    path('reviews', views.reviews),
    path('getPdfPage', views.getPdfPage, name='getPdfPage'),
    path('addReply/<int:feedbackId>', views.editreply),
    path('updatereply/<int:feedbackId>', views.updatereply)
]
