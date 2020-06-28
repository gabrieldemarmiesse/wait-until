import time
from wait_until import wait_until
import pytest


def some_function_that_cannot_work():
    raise ValueError("I cannot work!")


def test_wait_until_exception_raised():
    with pytest.raises(TimeoutError) as err:
        wait_until(some_function_that_cannot_work, timeout=1)

    assert "Timeout is 1s" in str(err.value)


class Dummy:
    def __init__(self):
        self.start_time = time.time()

    def is_loaded(self):
        if time.time() - self.start_time <= 1.5:
            raise ValueError("Not loaded yet!")
        return "Yay!"


def test_wait_until_is_loaded():
    dum = Dummy()

    result = wait_until(dum.is_loaded, timeout=2)
    assert result == "Yay!"
