from rest_framework import serializers 
from .models import FamilyComposition


class FamilyCompositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyComposition
        fields = '__all__'