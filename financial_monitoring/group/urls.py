from rest_framework.routers import DefaultRouter
from .views import GroupViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'group', GroupViewSet, basename='group')


urlpatterns = [
    path('', include(router.urls)),
]