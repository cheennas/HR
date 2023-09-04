from django.shortcuts import render
from rest_framework import viewsets
from .models import Courses
from .serializers import CoursesSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    lookup_field = 'iin'
 