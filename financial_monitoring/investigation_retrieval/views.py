from django.shortcuts import render
from rest_framework import viewsets
from .models import InvestigationRetrieval
from .serializers import InvestigationRetrievalSerializer


class InvestigationRetrievalViewSet(viewsets.ModelViewSet):
    queryset = InvestigationRetrieval.objects.all()
    serializer_class = InvestigationRetrievalSerializer