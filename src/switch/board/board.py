# from machine import Pin
#
# PIN_19 = Pin(19, Pin.OUT, Pin.PULL_DOWN)
# PIN_21 = Pin(21, Pin.OUT, Pin.PULL_DOWN)
# PIN_22 = Pin(22, Pin.OUT, Pin.PULL_DOWN)
# PIN_23 = Pin(23, Pin.OUT, Pin.PULL_DOWN)
from switch.board.pin import Pin


class Board:
    def __init__(self):
        self._pins = (Pin(19), Pin(21))

    def get_pin(self, pin):
        return self._pins[pin]

