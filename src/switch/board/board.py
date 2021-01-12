from switch.board.pin import Pin


class Board:
    SELECT_A = 0
    SELECT_B = 1
    SELECT_C = 2
    BUTTON_MUTE = 3
    BUTTON_LINE_1 = 4
    BUTTON_LINE_2 = 5
    LED_LINE_1 = 6
    LED_LINE_2 = 7
    LED_POWER = 8
    MUTE = 9

    _PIN_SELECT_A = 21
    _PIN_SELECT_B = 22
    _PIN_SELECT_C = 23
    _PIN_BUTTON_MUTE = 19
    _PIN_BUTTON_LINE_1 = 18
    _PIN_BUTTON_LINE_2 = 5
    _PIN_LED_POWER = 4
    _PIN_LED_LINE_1 = 0
    _PIN_LED_LINE_2 = 2
    _PIN_MUTE = 15

    def __init__(self):
        self._pins = [
            Pin(Board._PIN_SELECT_A),
            Pin(Board._PIN_SELECT_B),
            Pin(Board._PIN_SELECT_C),

            Pin(Board._PIN_BUTTON_MUTE, Pin.PULL_UP),
            Pin(Board._PIN_BUTTON_LINE_1, Pin.PULL_UP),
            Pin(Board._PIN_BUTTON_LINE_2, Pin.PULL_UP),

            Pin(Board._PIN_LED_LINE_1),
            Pin(Board._PIN_LED_LINE_2),
            Pin(Board._PIN_LED_POWER),

            Pin(Board._PIN_MUTE)
        ]

    def get_pin(self, pin):
        return self._pins[pin]
