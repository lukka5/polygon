import collections

from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models

from jsonfield import JSONField


class Provider(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = models.CharField(max_length=15, validators=[phone_validator])
    language = models.CharField(max_length=5, choices=settings.LANGUAGES)
    # http://www.xe.com/iso4217.php
    currency = models.CharField(max_length=3, validators=[RegexValidator(regex='^.{3}$',
                                message='Length has to be 3', code='nomatch')])


class Polygon(models.Model):
    provider = models.ForeignKey(Provider, related_name='polygons')
    name = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    polygon = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict})
