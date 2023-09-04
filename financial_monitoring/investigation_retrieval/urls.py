from rest_framework.routers import DefaultRouter
from .views import InvestigationRetrievalViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'investigation_retrieval', InvestigationRetrievalViewSet, basename='investigation_retrieval')


urlpatterns = [
    path('', include(router.urls)),
]
