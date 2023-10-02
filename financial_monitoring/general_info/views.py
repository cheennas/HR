from django.shortcuts import render
from rest_framework import viewsets
from .models import GeneralInfo
from .serializers import GeneralInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.response import Response


class GeneralInfoViewSet(viewsets.ModelViewSet):
    queryset = GeneralInfo.objects.all()
    serializer_class = GeneralInfoSerializer


class GeneralInfoAllView(APIView):
    def get(self, request, *args, **kwargs):
        general_info_all = GeneralInfo.objects.all()

        response_data = GeneralInfoSerializer(general_info_all, many=True).data

        return Response(response_data, status=status.HTTP_200_OK)
