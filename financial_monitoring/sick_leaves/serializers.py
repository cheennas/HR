from rest_framework import serializers 
from .models import SickLeaves


class SickLeavesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SickLeaves
        fields = '__all__'