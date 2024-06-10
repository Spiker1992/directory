from contextlib import contextmanager
from unittest import mock

@contextmanager
def catch_signal(signal):
    handler = mock.Mock()

    signal.connect(handler)
    yield handler
    signal.disconnect(handler)