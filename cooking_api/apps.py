from django.apps import AppConfig


class CookingApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cooking_api'

    def ready(self):
        from .signals import add_slug
