from rest_framework.routers import DefaultRouter
from .views import GroupViewSet
from django.urls import path, include
# from .views import GroupsView, GroupDetailsView

router = DefaultRouter()
router.register(r'group', GroupViewSet, basename='group')


urlpatterns = [
    path('', include(router.urls)),
]