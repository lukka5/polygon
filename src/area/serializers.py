from rest_framework import serializers
from rest_framework_gis.serializers import GeoModelSerializer

from .models import Polygon, Provider


class ProviderSerializer(serializers.ModelSerializer):
    polygons = serializers.PrimaryKeyRelatedField(many=True, queryset=Polygon.objects.all(), required=False)

    class Meta:
        model = Provider
        fields = ('id', 'name', 'email', 'phone', 'language', 'currency', 'polygons')


class PolygonSerializer(GeoModelSerializer):
    provider = serializers.ReadOnlyField(source='provider.name')

    class Meta:
        model = Polygon
        fields = ('id', 'name', 'price', 'polygon', 'provider')
