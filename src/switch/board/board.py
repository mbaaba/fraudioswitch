from switch.board.pin import Pin


class Board:
    def __init__(self):
        self._pins = (
            Pin(19),
            Pin(21),
            Pin(22, Pin.PULL_UP),  # Button_1
            Pin(23, Pin.PULL_UP)   # Button_2
        )

    def get_pin(self, pin):
        return self._pins[pin]
