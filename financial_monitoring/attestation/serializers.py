from rest_framework import serializers 
from .models import Attestation


class AttestationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attestation
        fields = '__all__'