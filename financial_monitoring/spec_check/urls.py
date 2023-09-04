from rest_framework.routers import DefaultRouter
from .views import SpecCheckViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'spec_check', SpecCheckViewSet, basename='spec_check')


urlpatterns = [
    path('', include(router.urls)),
] 
