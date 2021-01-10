from switch.board.board import Board
from switch.io.button import Button


class Switch:
    _active_line = 0

    def __init__(self):
        self._controller = Board()
        self._buttons = (
            Button(self._controller.get_pin(2)),
            Button(self._controller.get_pin(3))
        )

        self._buttons[0].set_handler(self._button_handler)
        self._buttons[1].set_handler(self._button_handler)

    def activate(self, line):
        if line <= 3:
            self._active_line = line
        else:
            self._active_line = 0

        if line == 1:
            self._controller.get_pin(0).on()
            self._controller.get_pin(1).off()
        elif line == 2:
            self._controller.get_pin(0).off()
            self._controller.get_pin(1).on()
        elif line == 3:
            self._controller.get_pin(0).on()
            self._controller.get_pin(1).on()
        else:
            self._controller.get_pin(0).off()
            self._controller.get_pin(1).off()

    def get_active_line(self):
        return self._active_line

    def _button_handler(self, button):
        if button.get_pin().get_id() == self._buttons[0].get_pin().get_id():
            self.activate(1)
        else:
            self.activate(2)
