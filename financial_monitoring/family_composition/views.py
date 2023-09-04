from django.shortcuts import render
from rest_framework import viewsets
from .models import FamilyComposition
from .serializers import FamilyCompositionSerializer


class FamilyCompositionViewSet(viewsets.ModelViewSet):
    queryset = FamilyComposition.objects.all()
    serializer_class = FamilyCompositionSerializer
    lookup_field = 'iin'