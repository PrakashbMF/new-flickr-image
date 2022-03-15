"""
    Data serializer module
"""
from rest_framework import serializers
from myapp.models import Location, Favourite, User


class UserSerializer(serializers.ModelSerializer):
    """
        Serialize User model
    """

    class Meta:
        """
            metaclass for user model
        """
        model = User
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    """
            Serialize Location model
        """

    class Meta:
        """
            metaclass for Location model
        """
        model = Location
        fields = "__all__"


class FavouriteSerializer(serializers.ModelSerializer):
    """
            Serialize Favourite model
        """

    class Meta:
        """
            metaclass for Favourite model
        """
        model = Favourite
        fields = "__all__"
