from rest_framework.routers import DefaultRouter
from .views import AcademicDegreeViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'academic_degree', AcademicDegreeViewSet, basename='academicdegree')


urlpatterns = [
    path('', include(router.urls)),
]
