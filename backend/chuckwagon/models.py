from django.contrib.gis.db import models
from django.utils.timezone import now # timezone depends on value of USE_TZ env variable
from django.utils import timezone


class Brand(models.Model):
    name = models.CharField(max_length=128, blank=False)
    twitter_handle = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=128, blank=False)
    area = models.MultiPolygonField()

    def __str__(self):
        return self.name


class TruckLocation(models.Model):
    class Meta:
        unique_together = (('brand', 'location', 'date'),)

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)
    date = models.DateField(editable=False)
    source_url = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return f'{self.brand} at {self.location} on {self.date}'

    def save(self, *args, **kwargs):
        self.date = self.date_time.date()
        super(TruckLocation, self).save(*args, **kwargs)


class LocationRegex(models.Model):
    class Meta:
        verbose_name_plural = 'location regexes'

    regex = models.CharField(max_length=256, blank=False, unique=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.location}: {self.regex}'
