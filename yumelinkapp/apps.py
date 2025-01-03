from django.apps import AppConfig

from yumelinkapp.utils import fetch_languages


class YumelinkappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'yumelinkapp'

    def ready(self):
        # Update the language choices when the server starts
        fetch_languages()
