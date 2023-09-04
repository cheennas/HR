from rest_framework.routers import DefaultRouter
from .views import ClassCategoryViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'class_category', ClassCategoryViewSet, basename='class_category')


urlpatterns = [
    path('', include(router.urls)),
]
