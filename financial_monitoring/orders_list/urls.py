from rest_framework.routers import DefaultRouter
# from .views import OrdersListView, OrdersListCreateView, OrdersListDestroyView, OrdersListUpdateView
from django.urls import path, include
from .views import OrdersListView


urlpatterns = [
    path('orders_list/create/', OrdersListView.as_view(), name='orders_create'),
    path('orders_list/get/<int:iin>/', OrdersListView.as_view(), name='orders_list_get'),
    path('orders_list/update/<int:pk>/', OrdersListView.as_view(), name='orders_update'),
    path('orders_list/delete/<int:pk>/', OrdersListView.as_view(), name='orders_delete'),
]

# urlpatterns = [
#     path('orders_list/get/<str:iin>/',
#          OrdersListView.as_view(), name="orders_list-get"),
#     path('orders_list/create/', OrdersListCreateView.as_view(),
#          name="orders_list-create"),
#     path('orders_list/update/<str:iin>/',
#          OrdersListUpdateView.as_view(), name="orders_list-update"),
#     path('orders_list/delete/<str:pk>/',
#          OrdersListDestroyView.as_view(), name="orders_list-delete"),
# ]