from rest_framework.routers import DefaultRouter
from .views import SportResultsViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'sport_results', SportResultsViewSet, basename='sportresults')


urlpatterns = [
    path('', include(router.urls)),
]