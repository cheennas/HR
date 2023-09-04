from django.shortcuts import render
from rest_framework import viewsets
from .models import OwningLanguages
from .serializers import OwningLanguagesSerializer


class OwningLanguagesViewSet(viewsets.ModelViewSet):
    queryset = OwningLanguages.objects.all()
    serializer_class = OwningLanguagesSerializer
    lookup_field = 'iin'
