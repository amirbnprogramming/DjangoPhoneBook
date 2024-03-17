from django.shortcuts import render
from rest_framework import generics, viewsets

from Contacts.models import Person
from Contacts.serializers import PersonSerializer
from Locations.models import City,State


# Create your views here.


# class AddressViewSetApiView(viewsets.ModelViewSet):
#     queryset = Address.get_all_objects()
#     serializer_class = AddressSerializer
#

class PersonViewSetApiView(viewsets.ModelViewSet):
    queryset = Person.get_all_objects()
    serializer_class = PersonSerializer
