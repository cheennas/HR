from django.urls import path
from . import views

urlpatterns = [
    path('photos/', views.PhotoView.as_view(), name='photos_list'),
    path('photos/<int:pk>', views.PhotoView.as_view(), name="photo_detail"),
]