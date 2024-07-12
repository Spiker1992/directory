

import uuid

from listing_management.event_stores.listing import ListingEventStore
from listing_management.settings.constants import EVENT_LISTING_PUBLISHED


def publish_listing(stream_id: uuid.UUID) -> None:
    event = ListingEventStore(
        stream_id=stream_id,
        event_type=EVENT_LISTING_PUBLISHED,
        event_payload={}
    )    
    event.save()