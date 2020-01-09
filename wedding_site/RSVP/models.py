import re
from django.db import models
from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from localflavor.us.models import USZipCodeField, USStateField

# Create your models here.

def validate_name(value):
    reg = re.compile('^[a-zA-Z][^#&<>\"~;$^%{}?]')
    if not reg.match(value) :
        raise ValidationError(u'%s name does not comply' % value)

class Guest(models.Model):
    first_name = models.CharField(max_length=30, validators=[validate_name])
    last_name = models.CharField(max_length=30, validators=[validate_name])
    address_street = models.TextField()
    address_city = models.CharField(max_length=15)
    address_state = USStateField()
    address_zip = USZipCodeField()
    address_country = CountryField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class GuestParty(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    party_first_name = models.CharField(max_length=30, validators=[validate_name])
    party_last_name = models.CharField(max_length=30, validators=[validate_name])

    def __str__(self):
        return "{} {}".format(self.party_first_name, self.party_last_name)
