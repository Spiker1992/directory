from dataclasses import asdict
import uuid
from django.test import TestCase
from listing_management.commands.create_listing import CreateListing, create_listing
from listing_management.event_stores.listing import ListingEventStore
from listing_management.read_models.listings import Listings
from listing_management.signals import listing_created
from listing_management.tests.utils import catch_signal
import pytest
from listing_management.settings.constants import DB_EVENT_STORE, DB_READ_MODEL, EVENT_LISTING_CREATED

@pytest.mark.django_db
class TestCreateListing(TestCase):
    databases = {DB_EVENT_STORE}

    def test_create_listing(self):
        listing_created.mock()
        payload = CreateListing(name="My Listing", description="Lorem Ipsum")

        stream_id = create_listing(payload)

        
        event = ListingEventStore.objects.get(stream_id=stream_id)

        assert event.event_payload == asdict(payload)
        listing_created.send.assert_called_with(instance=event, sender=ListingEventStore)
        listing_created.unmock()


@pytest.mark.django_db
class TestHandleListingCreatedEvent(TestCase):
    databases = {DB_READ_MODEL}

    def test_write_to_listings_model_on_listing_created_event(self):
        payload = CreateListing(name="My Listing", description="Lorem Ipsum")
        instance = ListingEventStore(
            stream_id=uuid.uuid4(), 
            event_type=EVENT_LISTING_CREATED, 
            event_payload=asdict(payload)
        )

        listing_created.send(sender=ListingEventStore, instance=instance)

        listing = Listings.objects.get(listing_uuid=instance.stream_id)

        assert listing.title == payload.name
        assert listing.description == payload.description