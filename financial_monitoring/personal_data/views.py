from django.shortcuts import render
from rest_framework import viewsets
from .models import PersonalData
from .serializers import PersonalDataSerializer


class PersonalDataViewSet(viewsets.ModelViewSet):
    queryset = PersonalData.objects.all()
    serializer_class = PersonalDataSerializer