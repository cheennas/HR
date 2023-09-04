from rest_framework import serializers
from .models import User
from general_info.models import GeneralInfo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
