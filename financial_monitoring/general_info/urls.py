from rest_framework.routers import DefaultRouter
from .views import GeneralInfoViewSet, GeneralInfoAllView
from django.urls import path, include

router = DefaultRouter()
router.register(r'general_info', GeneralInfoViewSet, basename='personaldata')


urlpatterns = [
    path('', include(router.urls)),
    path('general_info/all', GeneralInfoAllView.as_view(), name="general_info-get")
]
