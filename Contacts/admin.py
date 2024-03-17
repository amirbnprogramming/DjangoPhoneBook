from django.contrib import admin
from .models import Person

my_filter = ['is_active', 'created_at', 'updated_at', ]


# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'is_active', 'created_at', 'updated_at', ]
    list_editable = ['phone_number', 'is_active', ]
    list_display_links = ['first_name', 'last_name', ]
    search_fields = ['username', 'first_name', 'last_name', 'phone_number', ]
    list_filter = my_filter

#
# @admin.register(Address)
# class AddressAdmin(admin.ModelAdmin):
#     list_display = ['country', 'state', 'city', 'street', 'postal_code', 'is_active', 'created_at', 'updated_at', ]
#     list_editable = ['postal_code', 'is_active', ]
#     list_display_links = ['country', ]
#     search_fields = ['country', 'postal_code', ]
#     list_filter = my_filter
