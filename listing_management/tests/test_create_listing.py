from dataclasses import asdict
from django.test import TestCase
from listing_management.commands.create_listing import CreateListing, create_listing
from listing_management.event_stores.listing import ListingEventStore
from listing_management.signals import listing_created
from listing_management.tests.utils import catch_signal
import pytest


@pytest.mark.django_db
class TestCreateListing(TestCase):
    databases = {"event_store"}

    def test_create_listing(self):
        payload = CreateListing(name="My Listing", description="Lorem Ipsum")

        with catch_signal(listing_created) as signal:
            stream_id = create_listing(payload)

        signal.assert_called_once()
        
        event = ListingEventStore.objects.get(stream_id=stream_id)

        assert event.event_payload == asdict(payload)
