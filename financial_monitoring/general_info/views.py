from django.shortcuts import render
from rest_framework import viewsets
from .models import GeneralInfo
from .serializers import GeneralInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination


class GeneralInfoViewSet(viewsets.ModelViewSet):
    queryset = GeneralInfo.objects.all()
    serializer_class = GeneralInfoSerializer


class GeneralInfoAllView(ListAPIView):
    queryset = GeneralInfo.objects.all()
    serializer_class = GeneralInfoSerializer
    pagination_class = PageNumberPagination

