from .views import PersonalInfoAPIView
from django.urls import path, include

urlpatterns = [
    path('personal_info/<int:id>/',
         PersonalInfoAPIView.as_view(), name='personal_info'),
    path('personal_info/update/',
         PersonalInfoAPIView.as_view(), name='personal_info-update'),
    # path('personal_info/delete/<str:iin>/',
    #      PersonalInfoAPIView.as_view(), name='personal_info-delete'),
    path('personal_info/create/', PersonalInfoAPIView.as_view(),
         name='personal_info-create'),
]
