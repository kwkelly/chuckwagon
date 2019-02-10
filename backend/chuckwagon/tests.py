from django.test import TestCase
from .models import Brand, Location, LocationRegex, TruckLocation
from django.contrib.gis.geos import Polygon, MultiPolygon
from django.utils import timezone
from datetime import datetime
import re

# Create your tests here.


class BrandModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Brand.objects.create(name="Wang O'Reilly's", twitter_handle="@wangos")

    def test_brand_str_function(self):
        brand = Brand.objects.get(id=1)
        self.assertEqual(str(brand), "Wang O'Reilly's")


class LocationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        p1 = Polygon(((0, 0), (0, 1), (1, 1), (0, 0)))
        p2 = Polygon(((1, 1), (1, 2), (2, 2), (1, 1)))
        mp = MultiPolygon([p1, p2])
        Location.objects.create(name="Metro Center", area=mp)

    def test_location_str_function(self):
        loc = Location.objects.get(id=1)
        self.assertEqual(str(loc), "Metro Center")


class TruckLocationModelTest(TestCase):
    @classmethod
    def createTruckLocation(cls, name, location):
        # initialize brand
        regex = re.compile('[^a-zA-Z]')
        handle = regex.sub('', name)
        brand = Brand.objects.create(name=name, twitter_handle=f"@{handle}")

        #initialize Location
        p1 = Polygon(((0, 0), (0, 1), (1, 1), (0, 0)))
        p2 = Polygon(((1, 1), (1, 2), (2, 2), (1, 1)))
        mp = MultiPolygon([p1, p2])
        loc = Location.objects.create(name=location, area=mp)

        # datetime
        dt = timezone.make_aware(datetime.fromtimestamp(0))

        # and finally the truck location model
        tl = TruckLocation.objects.create(brand=brand, location=loc, date_time=dt, source_url="http://www.google.com")
        return tl

    @classmethod
    def setUpTestData(cls):
        cls.createTruckLocation("Wang O'Reilly's", "Metro Center")

    def test_save(self):
        # since we're using a custom ssave function
        tl = TruckLocation.objects.get(id=1)
        self.assertEqual(tl.brand.name, "Wang O'Reilly's")
        self.assertEqual(tl.location.name, "Metro Center")
        self.assertEqual(tl.source_url, "http://www.google.com")


    def test_date_datetime_equality(self):
        tl = TruckLocation.objects.get(id=1)
        self.assertEqual(tl.date, tl.date_time.date())

    def test_truck_location_str_function(self):
        tl = TruckLocation.objects.get(id=1)
        self.assertEqual(str(tl), "Wang O'Reilly's at Metro Center on 1970-01-01")
        
        

