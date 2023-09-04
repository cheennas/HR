from django.shortcuts import render
from rest_framework import viewsets
from .models import SportResults
from .serializers import SportResultSerializers


class SportResultsViewSet(viewsets.ModelViewSet):
    queryset = SportResults.objects.all()
    serializer_class = SportResultSerializers
    lookup_field = 'iin'
