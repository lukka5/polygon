import collections

from django.conf import settings
from django.core.validators import RegexValidator
from django.contrib.gis.db import models

from jsonfield import JSONField


class Provider(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    language = models.CharField(max_length=7, choices=settings.LANGUAGES)

    phone = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number format: '+999999999'. Up to 15 digits allowed.")])

    # ISO 4217 Currency Code (shttp://www.xe.com/iso4217.php)
    currency = models.CharField(max_length=3, validators=[RegexValidator(regex='^.{3}$',
                                message='Length has to be 3')])


class Polygon(models.Model):
    provider = models.ForeignKey(Provider, related_name='polygons')
    name = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    polygon = models.PolygonField()
