from rest_framework import serializers 
from .models import ClassCategory


class ClassCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassCategory
        fields = '__all__'