from decimal import Decimal

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Polygon, Provider
from .permissions import IsProviderOrReadOnly
from .serializers import PolygonSerializer, ProviderSerializer


class ProviderList(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class PolygonList(generics.ListCreateAPIView):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer

    def perform_create(self, serializer):
        # Super poor permission with only the provider's name
        try:
            provider = Provider.objects.get(name=self.request.data.get('provider', ''))
        except Provider.DoesNotExist:
            raise ValidationError('No provider with that name found')
        serializer.save(provider=provider)


class PolygonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer

    permission_classes = (IsProviderOrReadOnly,)


@api_view(['GET'])
def polygons_with_point(request, lat, lng):
    polygons = list()
    coordinate = [Decimal(lat), Decimal(lng)]

    for p in Polygon.objects.all():
        for hole in p.polygon['coordinates']:
            if coordinate in hole:
                polygons.append(p)

    serializer = PolygonSerializer(polygons, many=True)
    return Response(serializer.data)
