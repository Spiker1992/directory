from contextlib import contextmanager
from unittest.mock import Mock
from django.dispatch import Signal

class CustomSignal(Signal): 
    def mock(self):
        self.send = Mock()
        self.send_robust = Mock()

    def unmock(self):
        self.send = super().send
        self.send_robust = super().send_robust

    @classmethod
    @contextmanager
    def mock_all(cls):
        cls.mock(cls)
        yield
        cls.unmock(cls) 

# signal definition
order_submitted = CustomSignal()

# submit order command
def submit_order():
	# do import stuff...
	order_submitted.send("example", hello="world")

