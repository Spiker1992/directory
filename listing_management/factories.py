import uuid
import factory
from listing_management.event_stores.listing import ListingEventStore
from listing_management.read_models.listings import Listing
from listing_management.settings.constants import EVENT_LISTING_CREATED

class ListingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Listing

    listing_uuid = uuid.uuid4()
    title = "Foo"
    description = "Lorem Ipsum"


class DraftListingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ListingEventStore

    stream_id = uuid.uuid4()
    event_type = EVENT_LISTING_CREATED
    event_payload = {}