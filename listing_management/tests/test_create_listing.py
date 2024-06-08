from dataclasses import dataclass
from django.test import TestCase
from listing_management.signals import listing_created 
from django.dispatch import receiver
import uuid
import pytest
import time
from listing_management.event_stores.listing import ListingEventStore

@dataclass
class CreateListing:
    name: str 
    description: str

@pytest.mark.django_db
class TestCreateListing(TestCase):
    databases = {"event_store"}
    def test_create_listing(self):
        payload = CreateListing("name", "description")
        stream_id = uuid.uuid4()

        @receiver(listing_created, sender=ListingEventStore)
        def asser_signal_triggered(sender, **kwargs): 
            assert True

        create_listing(stream_id, payload)

        event = ListingEventStore.objects.get(stream_id=stream_id)
