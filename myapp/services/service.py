from datetime import datetime

from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response

from myapp.models import Location, Favourite


class LocationService:
    def __init__(self):
        pass

    def insert_location(self, location_name):
        print("************************************************")
        # print("loc in", location_name)
        gen_date = timezone.now()
        db_present_location_data = list(Location.objects.all().values_list("name", flat=True))
        # print("db_present_location_data", db_present_location_data)
        if location_name not in db_present_location_data:
            location_data = Location(name=location_name, genDate=gen_date)
            location_data.save()
            return location_name
        else:
            return location_name


class FavouriteImageService:
    def __init__(self):
        pass

    def get_favourites(self, user_id):
        user = User.objects.get(id=user_id)
        favourite_images = list(
            user.favourite_set.all().order_by("-genDate").values_list("image_url", flat=True))
        # favourite_images = [x.image_url for x in favourite_images_object]
        # favourite_images = ["https://live.staticflickr.com/65535/51096421190_667cbc0912_o.jpg",
        #                     "https://live.staticflickr.com/65535/51095616791_399ce1dbfa_o.jpg"]
        # favourite_images = []
        return favourite_images

    def insert_delete_image(self, user_id, image_url):
        print("user id in service : ", user_id)
        print("image_url in service : ", image_url)
        gen_date = timezone.now()
        fav_images = self.get_favourites(user_id)
        print("fav_images :", fav_images)
        user = User.objects.get(pk=user_id)
        print("user :", user)

        if image_url in fav_images:
            print("you are in if *******************************************")

            image_object = Favourite.objects.get(image_url=image_url, user=user)
            image_object.delete()
            # self.deleteFavouriteImage(user, image_url)
            return Response({"status": status.HTTP_204_NO_CONTENT})
        else:
            print("you are in else *******************************************")
            image_object = Favourite(image_url=image_url, user=user, genDate=gen_date)
            image_object.save()
            return Response({"status": status.HTTP_201_CREATED})
