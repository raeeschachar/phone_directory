from django import forms
from contacts.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
