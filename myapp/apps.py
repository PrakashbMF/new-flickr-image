"""This is for app config """
from django.apps import AppConfig


class MyappConfig(AppConfig):
    """
        config app here
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
