from django.shortcuts import render
from rest_framework import viewsets
from .models import AcademicDegree
from .serializers import AcademicDegreeSerializer


class AcademicDegreeViewSet(viewsets.ModelViewSet):
    queryset = AcademicDegree.objects.all()
    serializer_class = AcademicDegreeSerializer