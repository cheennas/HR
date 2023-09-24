from django.urls import path
from . import views

urlpatterns = [
    path('photos/', views.PhotoView.as_view(), name='photos_list'),
    path('photos/<int:id>', views.PhotoView.as_view(), name="photo_detail"),
    path('photos/delete/<int:photo_id>/', views.PhotoDeleteView.as_view(), name="photo_delete"),
]