from django.shortcuts import render
from rest_framework import viewsets
from .models import MilitaryRank
from .serializers import MilitaryRankSerializer


class MilitaryRankViewSet(viewsets.ModelViewSet):
    queryset = MilitaryRank.objects.all()
    serializer_class = MilitaryRankSerializer