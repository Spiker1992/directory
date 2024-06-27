import uuid

from listing_management.read_models.listings import Listings


def retrieve_listing(listing_uuid: uuid.UUID) -> Listings:
    return Listings.objects.get(listing_uuid=listing_uuid)