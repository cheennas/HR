from .views import StaffMainView
from django.urls import path

urlpatterns = [
    path('staff_main/create/', StaffMainView.as_view(),
         name='staff_main-create'),
]
