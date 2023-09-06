from rest_framework import serializers 
from .models import GeneralInfo
from family_composition.serializers import FamilyCompositionSerializer


class GeneralInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneralInfo
        fields = '__all__'