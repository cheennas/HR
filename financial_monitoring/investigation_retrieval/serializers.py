from rest_framework import serializers 
from .models import InvestigationRetrieval


class InvestigationRetrievalSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestigationRetrieval
        fields = '__all__'