from unittest.mock import Mock
from django.dispatch import Signal
from collections.abc import Callable
from typing import Any

class CustomSignals(Signal):
    @classmethod
    def mock(cls):
        cls.send = Mock()
        cls.send_robust = Mock()

    @classmethod
    def unmock(cls):
        cls.send = super().send
        cls.send_robust = super().send_robust



listing_created = CustomSignals()