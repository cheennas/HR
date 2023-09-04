from rest_framework.routers import DefaultRouter
from .views import CoursesViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'courses', CoursesViewSet, basename='courses')


urlpatterns = [
    path('', include(router.urls)),
]
