from rest_framework import serializers
from .models import Group
from general_info.models import GeneralInfo


class GroupSerializer(serializers.ModelSerializer):
    general_info = serializers.ListField(child=serializers.PrimaryKeyRelatedField(queryset=GeneralInfo.objects.all()), write_only=True)
    print(general_info)

    class Meta:
        model = Group
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        general_info_ids = validated_data.pop('general_info')
        group = Group.objects.create(**validated_data)
        group.general_info.set(general_info_ids)
        return group