from django.contrib import admin
from .models import OrdersList


@admin.register(OrdersList)
class OrdersListModelAdmin(admin.ModelAdmin):
    fields = ("iin", "order_type", "order_date", "types_of_order_types")
    list_display = ("id", "iin", "order_type", "order_date", "types_of_order_types")
    
    