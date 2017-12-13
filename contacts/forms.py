from django import forms

from contacts.models import Contact


class NewContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number']
