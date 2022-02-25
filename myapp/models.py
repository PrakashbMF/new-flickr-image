from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class ExtendedUser(models.Model):
    phone = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ExtendedUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.extendedUser.save()


class Location(models.Model):
    STATUS_CHOICES = (
        ("Y", "Yes"), ("N", "No")
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    genDate = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="Y")

    def __str__(self):
        return self.name


class Favourite(models.Model):
    STATUS_CHOICES = (
        ("Y", "Yes"), ("N", "No")
    )
    image_url = models.URLField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    genDate = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="Y")
