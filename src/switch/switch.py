from switch.board.board import Board
from switch.io.button import Button
from switch.io.input import Input

class Switch:
    _active_line = 0

    def __init__(self):
        self._controller = Board()

        self._lines = [
            Input((self._controller.get_pin(1), self._controller.get_pin(0)), (0, 1)),  # LINE 1
            Input((self._controller.get_pin(1), self._controller.get_pin(0)), (1, 0)),  # LINE 2
            Input((self._controller.get_pin(1), self._controller.get_pin(0)), (1, 1)),  # LINE 3
            Input((self._controller.get_pin(1), self._controller.get_pin(0)), (0, 0))   # OFF
        ]

        self._buttons = [
            Button(self._controller.get_pin(2)),
            Button(self._controller.get_pin(3)),
            Button(self._controller.get_pin(4)),
            Button(self._controller.get_pin(5))
        ]
        for btn in self._buttons:
            btn.set_handler(self._button_handler)

        self._leds = []
        for led in range(6, 10):
            curr_led = self._controller.get_pin(led)
            curr_led.off()
            self._leds.append(curr_led)
        self._leds[0].on()

    def activate(self, line):
        if self._active_line > 0:
            self._leds[self._active_line].off()

        if line <= 3:
            self._active_line = line
            self._leds[line].on()
        else:
            self._active_line = 0

        self._lines[line-1].activate()

    def get_active_line(self):
        return self._active_line

    def _button_handler(self, button):
        for i in range(4):
            if button.get_pin().get_id() == self._buttons[i].get_pin().get_id():
                self.activate(i+1)
                break
