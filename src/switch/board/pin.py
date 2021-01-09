from machine import Pin as BoardPin


class Pin:
    _board_pin = None

    def __init__(self, pin_id):
        self._id = pin_id
        self._board_pin = BoardPin(pin_id, BoardPin.OUT, BoardPin.PULL_DOWN)

    def get_id(self):
        return self._id

    def on(self):
        self._board_pin.value(1)

    def off(self):
        self._board_pin.value(0)

    def value(self):
        return self._board_pin.value(None)

    def irq(self, handler):
        self._board_pin.irq(handler)

