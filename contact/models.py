from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    phone_regex = RegexValidator(
            regex=r'^\+?1?\d{9,20}$',
            message="Phone number must be entered in the format: '+999999999'. Up to 20 digits allowed."
    )

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(validators=[phone_regex], max_length=20, blank=True)

    def __str__(self):
        return self.name
