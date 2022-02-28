from django.contrib import admin

# Register your models here.
from myapp.models import Favourite, Location, User

# ExtendedUser

admin.site.register(User)
admin.site.register(Location)
admin.site.register(Favourite)
