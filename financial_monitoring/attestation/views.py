from django.shortcuts import render
from rest_framework import viewsets
from .models import Attestation
from .serializers import AttestationSerializer


class AttestationViewSet(viewsets.ModelViewSet):
    queryset = Attestation.objects.all()
    serializer_class = AttestationSerializer