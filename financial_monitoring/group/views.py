from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Group
from .serializers import GroupSerializer
from general_info.models import GeneralInfo
from general_info.serializers import GeneralInfoSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        groups_with_general_info = []
        for group_data in serializer.data:
            group = Group.objects.get(pk=group_data['id'])
            connected_general_infos = GeneralInfo.objects.filter(group=group)
            connected_general_info_serializer = GeneralInfoSerializer(connected_general_infos, many=True)
            group_data['general_info'] = connected_general_info_serializer.data
            groups_with_general_info.append(group_data)

        return Response(groups_with_general_info)




