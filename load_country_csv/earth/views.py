from django.shortcuts import render
from django.http import HttpResponse
import csv

from .models import Country


def download(request, country_id):

    country = Country.objects.get(country_id=country_id).country
    filename = str(country) + ".csv"

    with open(filename, "w") as file:
        fieldnames = ["country", "id"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'country': country, 'id': country_id})

    with open(filename, 'r') as file:
        response = HttpResponse(file, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=' + filename
        return response


def map(request):
    return render(request, 'earth/map.html')
