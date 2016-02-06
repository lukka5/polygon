from django.conf.urls import url

from .views import ProviderDetail, ProviderList, PolygonList, PolygonDetail, polygons_with_point


urlpatterns = [
    url(r'^providers/$', ProviderList.as_view()),
    url(r'^providers/(?P<pk>[0-9]+)/$', ProviderDetail.as_view()),

    url(r'^polygons/$', PolygonList.as_view()),
    url(r'^polygons/(?P<pk>[0-9]+)/$', PolygonDetail.as_view()),

    # Get polygons which contain the given point
    url(r'^polygons/point/(?P<lat>-?\d+\.\d+)/(?P<lng>-?\d+\.\d+)/$', polygons_with_point),
]
