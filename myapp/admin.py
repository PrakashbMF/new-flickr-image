"""This is for URL Traversal """

from django.contrib import admin

from myapp.models import Favourite, Location, User

admin.site.register(User)
admin.site.register(Location)
admin.site.register(Favourite)
