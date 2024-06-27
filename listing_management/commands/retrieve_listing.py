import uuid

from listing_management.read_models.listings import Listing


def retrieve_listing(listing_uuid: uuid.UUID) -> Listing:
    return Listing.objects.get(listing_uuid=listing_uuid)