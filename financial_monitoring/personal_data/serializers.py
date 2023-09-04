from rest_framework import serializers 
from .models import PersonalData


class PersonalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = '__all__'