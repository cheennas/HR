from rest_framework import serializers
from .models import MilitaryRank


class MilitaryRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilitaryRank
        fields = '__all__'