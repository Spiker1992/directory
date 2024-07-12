import uuid
from django.test import TestCase

from listing_management.commands.publish_listing import publish_listing
from listing_management.event_stores.listing import ListingEventStore
from listing_management.factories import DraftListingFactory
from listing_management.settings.constants import DB_EVENT_STORE, EVENT_LISTING_CREATED, EVENT_LISTING_PUBLISHED
from listing_management.signals import CustomSignal


class TestListingPublish(TestCase):
    databases = { DB_EVENT_STORE }

    def test_listing_published(self):
        CustomSignal.mock()
        stream_id = uuid.uuid4()

        DraftListingFactory(stream_id=stream_id)

        publish_listing(stream_id)

        events = ListingEventStore.objects.all()

        assert len(events) == 2
        assert events[1].event_type == EVENT_LISTING_PUBLISHED

        CustomSignal.send.assert_called_with(instance=events[1], sender=ListingEventStore)

        CustomSignal.unmock_all()