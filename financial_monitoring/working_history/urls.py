# from rest_framework.routers import DefaultRouter
# from .views import WorkingHistoryListView, WorkingHistoryCreateView, WorkingHistoryUpdateView, WorkingHistoryDestroyView
# from django.urls import path, include
#
#
# urlpatterns = [
#     path('working_history/get/<str:iin>/',
#          WorkingHistoryListView.as_view(), name='working_history-get'),
#     path('working_history/create/', WorkingHistoryCreateView.as_view(), name='working_history-create'),
#     path('working_history/update/<str:iin>/', WorkingHistoryUpdateView.as_view(), name='working_history-update'),
#     path('working_history/delete/<str:iin>/', WorkingHistoryDestroyView.as_view(), name='working_history-delete'),
#
# ]

from django.urls import path, include
from .views import WorkingHistoryView


urlpatterns = [
    path('working_history/create/', WorkingHistoryView.as_view(), name='working_history_create'),
    path('working_history/get/<int:iin>/', WorkingHistoryView.as_view(), name='working_history_get'),
    path('working_history/update/<int:pk>/', WorkingHistoryView.as_view(), name='working_history_update'),
    path('working_history/delete/<int:pk>/', WorkingHistoryView.as_view(), name='working_history_delete'),
]
