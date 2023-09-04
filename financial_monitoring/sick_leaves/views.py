from django.shortcuts import render
from rest_framework import viewsets
from .models import SickLeaves
from .serializers import SickLeavesSerializer


class SickLeavesViewSet(viewsets.ModelViewSet):
    queryset = SickLeaves.objects.all()
    serializer_class = SickLeavesSerializer