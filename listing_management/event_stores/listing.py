from listing_management.settings.constants import EVENT_LISTING_CREATED
from modules.commons.event_store_model import EventStoreModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from listing_management.signals import listing_created 

class ListingEventStore(EventStoreModel):
    pass

@receiver(post_save, sender=ListingEventStore)
def my_handler(sender, **kwargs): 
    if kwargs["instance"].event_type == EVENT_LISTING_CREATED:
        listing_created.send(sender=sender, instance=kwargs["instance"])