from rest_framework.routers import DefaultRouter
from .views import MilitaryRankViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'military_rank', MilitaryRankViewSet, basename='military_rank')


urlpatterns = [
    path('', include(router.urls)),
]
