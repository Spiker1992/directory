from dataclasses import asdict, dataclass
import uuid
from listing_management.settings.constants import EVENT_LISTING_CREATED
from listing_management.event_stores.listing import ListingEventStore

@dataclass
class CreateListing:
    name: str
    description: str

def create_listing(payload: CreateListing) -> uuid.UUID:
    stream_id = uuid.uuid4()
    
    event = ListingEventStore(
        stream_id=stream_id, 
        event_payload=asdict(payload), 
        event_type=EVENT_LISTING_CREATED
    )
    event.save()

    return stream_id