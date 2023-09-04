from rest_framework import serializers 
from .models import SportResults


class SportResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = SportResults
        fields = '__all__'