from rest_framework.routers import DefaultRouter
from .views import SickLeavesViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'sick_leaves', SickLeavesViewSet, basename='sick_leaves')


urlpatterns = [
    path('', include(router.urls)),
]
