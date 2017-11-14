from django.conf.urls import url

from .views import map, download

urlpatterns = [
    url(r'^map', map, name="map"),
    url(r'^(?P<country_id>[A-Z]{3})/', download, name="download"),
]
