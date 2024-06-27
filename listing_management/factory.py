
import uuid
import factory
from listing_management.read_models.listings import Listing


class ListingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Listing
    
    listing_uuid = uuid.uuid4()
    title = "FooBar"
    description = "Lorem Ipsum"