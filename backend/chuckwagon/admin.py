from django.contrib import admin
from .models import Location, Brand, TruckLocation, LocationRegex

# Register your models here.

admin.site.register(Location)
admin.site.register(LocationRegex)
admin.site.register(Brand)
admin.site.register(TruckLocation)
