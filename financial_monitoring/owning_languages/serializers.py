from rest_framework import serializers 
from .models import OwningLanguages


class OwningLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwningLanguages
        fields = '__all__'