from django.test import TestCase
import pytest
from listing_management.commands.retrieve_listing import retrieve_listing
from listing_management.factories import ListingFactory
from listing_management.settings.constants import DB_READ_MODEL

@pytest.mark.django_db
class TestListingRetrieval(TestCase):
    databases = {DB_READ_MODEL}

    def test_retrieve_a_listing(self):
        # we need a listing
        listing = ListingFactory()

        # call a command
        actual = retrieve_listing(listing.listing_uuid)

        # verify that command return correct output
        assert actual.title == listing.title
        assert actual.description == listing.description