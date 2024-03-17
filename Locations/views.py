from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Country, State, City
from .serializers import CountrySerializer, StateSerializer, CitySerializer


# Create your views here.


class CountryViewSetApiView(viewsets.ReadOnlyModelViewSet):
    queryset = Country.get_all_objects()
    serializer_class = CountrySerializer
    pagination_class = PageNumberPagination


class StateViewSetApiView(viewsets.ReadOnlyModelViewSet):
    queryset = State.get_all_objects()
    serializer_class = StateSerializer
    pagination_class = PageNumberPagination


class CityViewSetApiView(viewsets.ReadOnlyModelViewSet):
    queryset = City.get_all_objects()
    serializer_class = CitySerializer
    pagination_class = PageNumberPagination
