from rest_framework.routers import DefaultRouter
from .views import PersonalDataViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'personal_data', PersonalDataViewSet, basename='personaldata')


urlpatterns = [
    path('', include(router.urls)),
]