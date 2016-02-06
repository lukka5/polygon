from django.conf.urls import include, url

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^', include('area.urls')),
    url(r'^docs/', include('rest_framework_docs.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
