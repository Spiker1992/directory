
from dataclasses import asdict
from django.test import TestCase
from listing_management.commands.create_listing import CreateListing, create_listing
from listing_management.signals import listing_created 
import uuid
from listing_management.tests.utils import catch_signal
import pytest
from unittest import mock
from listing_management.event_stores.listing import ListingEventStore


@pytest.mark.django_db
class TestCreateListing(TestCase):
    databases = {"event_store"}

    def test_create_listing(self):
        payload = CreateListing("name", "description")
        stream_id = uuid.uuid4()

        with catch_signal(listing_created) as signal:
            create_listing(stream_id, payload)  

        event = ListingEventStore.objects.get(stream_id=stream_id)

        assert event.event_payload == asdict(payload)
        signal.assert_called_once_with(
            signal=mock.ANY,  
            sender=ListingEventStore,  
            instance=event
        )
