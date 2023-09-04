from django.shortcuts import render
from rest_framework import viewsets
from .models import Awards
from .serializers import AwardsSerializer


class AwardsViewSet(viewsets.ModelViewSet):
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer