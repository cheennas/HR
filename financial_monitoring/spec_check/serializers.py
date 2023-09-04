from rest_framework import serializers 
from .models import SpecCheck


class SpecCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecCheck
        fields = '__all__'