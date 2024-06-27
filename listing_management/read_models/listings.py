from django.db import models
from listing_management.event_stores.listing import ListingEventStore
from listing_management.signals import listing_created
from django.dispatch import receiver

class Listing(models.Model):
    listing_uuid = models.UUIDField(primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    

@receiver(listing_created, sender=ListingEventStore)
def handle_listing_created(sender, instance, **kwargs):
    Listing(
        listing_uuid=instance.stream_id,
        title=instance.event_payload["name"],
        description=instance.event_payload["description"],  
    ).save()