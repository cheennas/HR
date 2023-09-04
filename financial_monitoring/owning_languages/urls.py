from rest_framework.routers import DefaultRouter
from .views import OwningLanguagesViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'owning_languages', OwningLanguagesViewSet, basename='owninglanguages')


urlpatterns = [
    path('', include(router.urls)),
]