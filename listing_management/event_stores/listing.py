from modules.commons.event_store_model import EventStoreModel
from listing_management.settings.constants import EVENT_LISTING_CREATED
from listing_management.signals import listing_created
from django.dispatch import receiver
from django.db.models.signals import post_save

class ListingEventStore(EventStoreModel):
    pass

@receiver(post_save, sender=ListingEventStore)
def handle_listing_created(sender, instance, **kwargs):
    if instance.event_type == EVENT_LISTING_CREATED:
        listing_created.send(sender=sender, instance=instance)