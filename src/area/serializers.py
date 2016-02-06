from rest_framework import serializers

from .models import Polygon, Provider


class ProviderSerializer(serializers.ModelSerializer):
    polygons = serializers.PrimaryKeyRelatedField(many=True, queryset=Polygon.objects.all())

    class Meta:
        model = Provider
        fields = ('id', 'name', 'email', 'phone', 'language', 'currency', 'polygons')


class PolygonSerializer(serializers.ModelSerializer):
    provider = serializers.ReadOnlyField(source='provider.name')
    polygon = serializers.JSONField()

    class Meta:
        model = Polygon
        fields = ('id', 'name', 'price', 'polygon', 'provider')
