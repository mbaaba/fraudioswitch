from switch.board.board import Board


class Switch:
    def __init__(self):
        self._board = Board()

    def activate(self, line):
        if line == 1:
            self._board.get_pin(0).on()
            self._board.get_pin(1).off()
        elif line == 2:
            self._board.get_pin(0).off()
            self._board.get_pin(1).on()
        elif line == 3:
            self._board.get_pin(0).on()
            self._board.get_pin(1).on()
        else:
            self._board.get_pin(0).off()
            self._board.get_pin(1).off()
