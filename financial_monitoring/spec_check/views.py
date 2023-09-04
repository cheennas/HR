from django.shortcuts import render
from rest_framework import viewsets
from .models import SpecCheck
from .serializers import SpecCheckSerializer


class SpecCheckViewSet(viewsets.ModelViewSet):
    queryset = SpecCheck.objects.all()
    serializer_class = SpecCheckSerializer