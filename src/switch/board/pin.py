from machine import Pin as BoardPin


class Pin:
    PULL_UP = BoardPin.PULL_UP
    PULL_DOWN = BoardPin.PULL_DOWN

    _board_pin = None

    def __init__(self, pin_id, pull=BoardPin.PULL_DOWN):
        self._id = pin_id
        self._board_pin = BoardPin(pin_id, BoardPin.OUT, pull)

    def get_id(self):
        return self._id

    def on(self):
        self._board_pin.value(1)

    def off(self):
        self._board_pin.value(0)

    def value(self, x=None):
        return self._board_pin.value(x)

    def irq(self, handler):
        self._board_pin.irq(handler)
