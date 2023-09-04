from rest_framework.routers import DefaultRouter
from .views import FamilyCompositionViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'family_composition', FamilyCompositionViewSet, basename='familycomposition')


urlpatterns = [
    path('', include(router.urls)),
]