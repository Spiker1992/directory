import uuid
from dataclasses import asdict, dataclass
from listing_management.settings.constants import EVENT_LISTING_CREATED
from listing_management.event_stores.listing import ListingEventStore

@dataclass
class CreateListing:
    name: str 
    description: str

def create_listing(stream_id: uuid.UUID, payload: CreateListing):
    ListingEventStore(stream_id=stream_id, event_type=EVENT_LISTING_CREATED, event_payload=asdict(payload)).save()
