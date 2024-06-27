
import uuid
import factory
from listing_management.read_models.listings import Listings


class ListingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Listings
    
    listing_uuid = uuid.uuid4()
    title = "FooBar"
    description = "Lorem Ipsum"