from django.shortcuts import render
from rest_framework import viewsets
from .models import Education
from .serializers import EducationSerializer


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    lookup_field = 'iin'
