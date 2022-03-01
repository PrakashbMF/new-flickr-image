from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from .managers import UserManager


# from django.utils.translation import ugettext_lazy as _
# Create your models here.


#
# class ExtendedUser(models.Model):
#     phone = models.CharField(max_length=10, null=True)
#     age = models.IntegerField(null=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     # @receiver(post_save, sender=User)
#     # def create_user_profile(sender, instance, created, **kwargs):
#     #     if created:
#     #         ExtendedUser.objects.create(user=instance)
#     #
#     # @receiver(post_save, sender=User)
#     # def save_user_profile(sender, instance, **kwargs):
#     #     instance.extendedUser.save()


class User(AbstractBaseUser, PermissionsMixin):
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

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name


class Location(models.Model):
    STATUS_CHOICES = (
        ("Y", "Yes"), ("N", "No")
    )
    name = models.CharField(max_length=100)
    genDate = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="Y")

    def __str__(self):
        return self.name


class Favourite(models.Model):
    STATUS_CHOICES = (
        ("Y", "Yes"), ("N", "No")
    )
    image_url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genDate = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="Y")
