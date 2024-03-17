from rest_framework import serializers
from .models import Person
from Locations.models import Country, State, City


class PersonSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        permited_states = State.objects.filter(country__name=attrs['country']).all()
        permited_cities = City.objects.filter(state__name=attrs['state']).all()
        selected_country = Country.objects.get(name=attrs['country'])
        print("states:", permited_states)
        print("cities:", permited_cities)
        print(attrs['state'])
        print(attrs['city'])

        if attrs['state'] not in permited_states:
            raise serializers.ValidationError("Please consider Country while selecting State.")

        if attrs['city'] not in permited_cities:
            raise serializers.ValidationError("Please consider State while selecting City.")

        if not attrs['phone_number'].isdigit():
            raise serializers.ValidationError("phone number must contain only numbers.")

        if len(attrs['phone_number']) > 18 or len(attrs['phone_number']) < 4:
            raise serializers.ValidationError("phone number without Country-Code must be at least 4 and at most 18 "
                                              "characters.")

        if Person.objects.filter(phone_number=attrs['phone_number']).exists():
            raise serializers.ValidationError("phone number exists.")
        else:
            prefix_number = '+' + selected_country.phone_code
            attrs['phone_number'] = prefix_number + attrs['phone_number']
            return super().validate(attrs)

    class Meta:
        model = Person
        fields = Person.get_list_fields()
