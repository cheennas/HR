from rest_framework import serializers 
from .models import Autobiography


class AutobiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Autobiography
        fields = '__all__'