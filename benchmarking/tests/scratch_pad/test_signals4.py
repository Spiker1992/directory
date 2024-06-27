from listing_management.tests.scratch_pad.signals import CustomSignal, submit_order

def test_one_signal_doesnt_impact_another_signal():
    with CustomSignal.mock_all():
        submit_order()

        CustomSignal.send.assert_called_once_with("example", hello="world")