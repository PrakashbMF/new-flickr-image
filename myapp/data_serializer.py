from django.contrib.auth.models import User
from rest_framework import serializers
from myapp.models import Location, Favourite, ExtendedUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ("name", "email", "phone")
        fields = "__all__"


class ExtendedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        # fields = ("name", "email", "phone")
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        # fields = ("name", "email", "phone")
        fields = "__all__"


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        # fields = ("name", "email", "phone")
        fields = "__all__"
