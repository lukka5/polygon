from django.contrib.gis.geos import Point

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
    point = Point(float(lat), float(lng))

    # Maybe? Is this is '__contains' of Geos or Django's orm?
    # Seems to be the one from Geos:
    #     https://docs.djangoproject.com/en/1.9/ref/contrib/gis/geoquerysets/#contains
    polygons = Polygon.objects.filter(polygon__contains=point)

    serializer = PolygonSerializer(polygons, many=True)
    return Response(serializer.data)
