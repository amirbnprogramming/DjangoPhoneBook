from django.contrib import admin
from Locations.models import Country, State, City

name_field = ['name', ]


# Register your models here.
class BaseAdminModel(admin.ModelAdmin):
    list_display_links = name_field


@admin.register(Country)
class CountryAdmin(BaseAdminModel):
    list_display = Country.get_list_fields()
    search_fields = list_display
    list_editable = ['iso_name', 'phone_code', ]


@admin.register(State)
class StateAdmin(BaseAdminModel):
    list_display = State.get_list_fields()
    list_editable = ['country', ]
    search_fields = list_display


@admin.register(City)
class CityAdmin(BaseAdminModel):
    list_display = City.get_list_fields()
    list_editable = ['state', ]
    search_fields = list_display
