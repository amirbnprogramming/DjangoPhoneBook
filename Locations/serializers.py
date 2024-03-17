from rest_framework import serializers
from .models import Country, State, City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = model.get_list_fields()


class StateSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)

    class Meta:
        model = State
        fields = model.get_list_fields() + ['cities']


class CountrySerializer(serializers.ModelSerializer):
    states = StateSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = model.get_list_fields() + ['states']
