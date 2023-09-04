from .views import StaffInfoAPIView
from django.urls import path, include

urlpatterns = [
    path('staff_info/<int:id>/',
         StaffInfoAPIView.as_view(), name='staff_info-get'),
    path('staff_info/update/',
         StaffInfoAPIView.as_view(), name='staff_info-update'),
    # path('staff_info/delete/<str:iin>/',
    #      StaffInfoAPIView.as_view(), name='staff_info-delete'),
    path('staff_info/create/',
         StaffInfoAPIView.as_view(), name='staff_info-create'),
]

