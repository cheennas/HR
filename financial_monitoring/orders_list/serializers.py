from rest_framework import serializers 
from .models import OrdersList


class OrdersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersList
        fields = '__all__'