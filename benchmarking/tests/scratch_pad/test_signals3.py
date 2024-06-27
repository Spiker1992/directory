from listing_management.tests.scratch_pad.signals import order_submitted, submit_order

def test_one_signal_doesnt_impact_another_signal():
    order_submitted.mock()

    submit_order()

    order_submitted.send.assert_called_once_with("example", hello="world")
    order_submitted.unmock()