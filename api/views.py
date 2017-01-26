from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer


class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class ProvinceViewSet(viewsets.ModelViewSet):

    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
