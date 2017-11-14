from django.db import models


class Country(models.Model):
    country_id = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return "%s, %s" % (self.country, self.country_id)

