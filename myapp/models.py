"""This model represents Database table """

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
        User model, and it is an AbstractBaseUser.it holds registered user
    """
    email = models.EmailField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=10, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """
            Returns the first_name plus the last_name, with a space in between.
        """
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    class Meta:
        """
            metaclass for user
        """
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Location(models.Model):
    """
           Location model where we can store locations
    """
    STATUS_CHOICES = (
        ("Y", "Yes"), ("N", "No")
    )
    name = models.CharField(max_length=100)
    gen_date = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="Y")

    def __str__(self):
        return str(self.name)


class Favourite(models.Model):
    """
           Favourite model where we can store liked images
    """
    STATUS_CHOICES = (
        ("Y", "Yes"), ("N", "No")
    )
    image_url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gen_date = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="Y")
