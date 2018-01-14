from django import forms
from django.contrib.auth.forms import UserCreationForm

from contacts.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
