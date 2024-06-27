from unittest.mock import Mock, patch
from django.dispatch import Signal
from collections.abc import Callable
from typing import Any
from functools import partial

class CustomSignal(Signal):
    def mock(self):
        self.send = Mock()
        self.send_robust = Mock()


    @classmethod
    def mock(cls):
        cls.send = Mock()
        cls.send_robust = Mock()


    def unmock(self):
        self.send = super().send
        self.send_robust = super().send_robust

    @classmethod
    def unmock_all(cls):
        cls.send = super().send
        cls.send_robust = super().send_robust

    



listing_created = CustomSignal()

