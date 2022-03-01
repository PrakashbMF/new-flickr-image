from datetime import datetime

from django.utils import timezone
from geopy.geocoders import Nominatim
from rest_framework import status
from rest_framework.response import Response

from myapp.models import Location, Favourite, User


class GeoLocation:
    def __init__(self):
        pass

    def getGeoLocation(self, latitude, longitude):
        geolocator = Nominatim(user_agent="myGeocoder")
        location = geolocator.reverse(latitude + "," + longitude)
        # print("geo locations location", location)
        if location is not None:
            address = location.raw['address']
            city = address.get('city', '')
            state = address.get('state', '')
            country = address.get('country', '')
            code = address.get('country_code')
            zipcode = address.get('postcode')
            # print("geo locations:", address)
            # print("geo city:", city)
            # print("geo state:", state)
            # print("geo country:", country)

            if city:
                return city
            elif not city:
                # print(state)
                return state
            else:
                # print(country)
                return country
        else:
            return None
