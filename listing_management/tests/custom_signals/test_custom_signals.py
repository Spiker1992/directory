from unittest.mock import Mock
from listing_management.tests.custom_signals.signal1 import signal1
from listing_management.tests.custom_signals.signal2 import signal2
from listing_management.signals import CustomSignal


def test_mock_all_signals():
    CustomSignal.mock_all()

    signal2.send(sender="dummy")

    
    signal1.send.assert_called_once()
    CustomSignal.send.assert_called_once()

    CustomSignal.unmock_all()


def test_mix_mock_with_unmock_all():
    signal2.mock()

    CustomSignal.unmock_all()
    
    assert isinstance(signal2.send, Mock) is False


def test_one_signal_doesnt_impact_another_signal():
    signal2.mock()

    signal2.send(sender="mocked_send")
    signal1.send(sender="not_mocked_send")

    assert isinstance(signal1.send, Mock) is False
    assert isinstance(signal2.send, Mock) is True
    signal2.send.assert_called_once_with(sender="mocked_send")