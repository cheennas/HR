from rest_framework.routers import DefaultRouter
from .views import AutobiographyViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'autobiography', AutobiographyViewSet, basename='autobiography')


urlpatterns = [
    path('', include(router.urls)),
]
