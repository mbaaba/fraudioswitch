from switch.board.pin import Pin


class Board:
    def __init__(self):
        self._pins = [
            Pin(19),                # Selection bit 0
            Pin(21),                # Selection bit 1

            Pin(22, Pin.PULL_UP),   # Button_0
            Pin(23, Pin.PULL_UP),   # Button_1
            Pin(18, Pin.PULL_UP),   # Button_2
            Pin(5, Pin.PULL_UP),    # Button_3

            Pin(4),                 # Power LED
            Pin(0),                 # LED_1
            Pin(2),                 # LED_2
            Pin(15)                 # LED_3
        ]

    def get_pin(self, pin):
        return self._pins[pin]
