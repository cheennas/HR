from rest_framework.routers import DefaultRouter
from .views import AwardsViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'awards', AwardsViewSet, basename='awards')


urlpatterns = [
    path('', include(router.urls)),
]
