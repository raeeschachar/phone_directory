from django import forms

from contacts.models import Contact, Address


class NewContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'contact_image']


class NewAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['contact', 'address_selection', 'address_line', 'city', 'state', 'zip_code', 'country']
