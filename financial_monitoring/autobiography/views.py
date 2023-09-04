from django.shortcuts import render
from rest_framework import viewsets
from .models import Autobiography
from .serializers import AutobiographySerializer


class AutobiographyViewSet(viewsets.ModelViewSet):
    queryset = Autobiography.objects.all()
    serializer_class = AutobiographySerializer