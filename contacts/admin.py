from django.contrib import admin
from .models import Contact, Address


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'user']


class AddressInline(admin.TabularInline):
    list_display = ['address_line', 'city', 'state', 'zip', 'country']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Address)
