from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    phone_regex = RegexValidator(
            regex=r'^\+?1?\d{9,20}$',
            message="Phone number must be entered in the format: '+999999999'. Up to 20 digits allowed."
    )

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(validators=[phone_regex], max_length=20, blank=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    HOME = 'home'
    OFFICE = 'office'

    ADDRESS_CHOICES = (
        (HOME, 'Home Address'),
        (OFFICE, 'Office Address'),
    )

    contact = models.ForeignKey(Contact)
    address_selection = models.CharField(max_length=6, choices=ADDRESS_CHOICES, default=HOME)
    address_line = models.CharField(max_length=50)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=15)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.country
