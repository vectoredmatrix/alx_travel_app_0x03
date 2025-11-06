from django.apps import AppConfig

class ListingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alx_travel_app.listings'  # ✅ match INSTALLED_APPS

    def ready(self):
        import alx_travel_app.listings.signals  # ✅ match full path
