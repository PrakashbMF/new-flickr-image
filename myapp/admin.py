from django.contrib import admin

# Register your models here.
from myapp.models import Favourite, Location, ExtendedUser

admin.site.register(ExtendedUser)
admin.site.register(Location)
admin.site.register(Favourite)
