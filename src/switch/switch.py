from switch.board.board import Board
from switch.io.button import Button
from switch.io.input import Input


class Switch:
    LINE_1 = 0
    LINE_2 = 1
    MUTE = 2

    BUTTON_LINE_1 = 0
    BUTTON_LINE_2 = 1
    BUTTON_MUTE = 2

    LED_LINE_1 = 0
    LED_LINE_2 = 1
    LED_POWER = 2

    def __init__(self):
        self._controller = Board()

        self._init_lines()
        self._init_buttons()
        self._init_leds()

        self._mute_pin = self._controller.get_pin(Board.MUTE)
        self._active_line = Switch.MUTE
        self._mute()

    def _init_leds(self):
        self._leds = []
        for led in range(Board.LED_LINE_1, Board.LED_POWER + 1):
            curr_led = self._controller.get_pin(led)
            curr_led.off()
            self._leds.append(curr_led)
        self._leds[Switch.LED_POWER].on()

    def _button_handler(self, button):
        for i in range(len(self._buttons)):
            if button.get_pin().get_id() == self._buttons[i].get_pin().get_id():
                self.activate(i)
                break

    def _init_buttons(self):
        self._buttons = [
            Button(self._controller.get_pin(Board.BUTTON_LINE_1)),
            Button(self._controller.get_pin(Board.BUTTON_LINE_2)),
            Button(self._controller.get_pin(Board.BUTTON_MUTE))
        ]
        for btn in self._buttons:
            btn.set_handler(self._button_handler)

    def _init_lines(self):
        self._lines = [
            Input([
                self._controller.get_pin(Input.WIRE_1),
                self._controller.get_pin(Input.WIRE_2),
                self._controller.get_pin(Input.WIRE_3)
            ], [0, 0, 0]),  # LINE 1
            Input([
                self._controller.get_pin(Input.WIRE_1),
                self._controller.get_pin(Input.WIRE_2),
                self._controller.get_pin(Input.WIRE_3)
            ], [1, 1, 1])  # LINE 2
        ]

    def activate(self, line):
        if self._active_line < Switch.MUTE:
            self._leds[self._active_line].off()

        if line <= Switch.LINE_2:
            self._active_line = line
            self._leds[line].on()
            self._unmute()
            self._lines[line].activate()
        else:
            self._active_line = Switch.MUTE
            self._mute()

    def _mute(self):
        self._mute_pin.on()

    def _unmute(self):
        self._mute_pin.off()

    def get_active_line(self):
        return self._active_line

