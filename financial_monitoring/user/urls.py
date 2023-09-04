from .views import UserAPIView
from django.urls import path

urlpatterns = [
    path('user/create/', UserAPIView.as_view(), name='user-create'),
]