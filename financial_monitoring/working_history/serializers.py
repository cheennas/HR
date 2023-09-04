from rest_framework import serializers 
from .models import WorkingHistory


class WorkingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingHistory
        fields = '__all__'
        
        