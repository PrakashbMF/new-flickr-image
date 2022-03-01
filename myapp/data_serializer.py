from rest_framework import serializers
from myapp.models import Location, Favourite, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = "__all__"
