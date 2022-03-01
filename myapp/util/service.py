from geopy.geocoders import Nominatim


class GeoLocation:
    def __init__(self):
        pass

    def get_geo_location(self, latitude, longitude):
        geolocator = Nominatim(user_agent="myGeocoder")
        location = geolocator.reverse(latitude + "," + longitude)
        if location is not None:
            address = location.raw['address']
            city = address.get('city', '')
            state = address.get('state', '')
            country = address.get('country', '')
            code = address.get('country_code')
            zipcode = address.get('postcode')

            if city:
                return city
            elif not city:
                return state
            else:
                return country
        else:
            return None
