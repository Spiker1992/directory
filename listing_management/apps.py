from django.apps import AppConfig

from listing_management.settings.constants import APP_NAME


class ListingManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = APP_NAME
