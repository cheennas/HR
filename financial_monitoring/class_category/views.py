from django.shortcuts import render
from rest_framework import viewsets
from .models import ClassCategory
from .serializers import ClassCategorySerializer


class ClassCategoryViewSet(viewsets.ModelViewSet):
    queryset = ClassCategory.objects.all()
    serializer_class = ClassCategorySerializer