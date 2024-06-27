from listing_management.tests.scratch_pad.signals import order_submitted, submit_order

def test_submit_order():
	# setup
	sender_called = False
	def mock_receiver(**kwargs):
		nonlocal sender_called
		sender_called = True
		
	order_submitted.connect(mock_receiver)
	
	# run command
	submit_order()
	
	# assertions...
	assert sender_called == True
	
	order_submitted.disconnect(mock_receiver)