from .views import ReportListAPIView
from django.urls import path, include

urlpatterns = [
    path('report_list/',
         ReportListAPIView.as_view(), name='report_list'),
]
