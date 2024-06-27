from unittest.mock import patch
from listing_management.tests.scratch_pad.signals import submit_order


def test_submit_order():
	# setup
	# ...

	# run command
	with patch("listing_management.tests.scratch_pad.signals.handle_order_confirmation") as mock:
		submit_order()
		
	# assertions...
	mock.assert_called_once()