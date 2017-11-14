import os
import json

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = "footest.settings"
application = get_wsgi_application()

from earth.models import Country

file = "static/countries.geo.json"
with open(file, "r") as caps:
    dump = json.load(caps)

for doc in dump["features"]:
    country = Country(country=doc["properties"]["name"],
                      country_id=doc["id"])

    if not Country.objects.filter(country_id=country.country_id).exists():
        country.save()
