class Button:
    def __init__(self, pin):
        self._pin = pin

    def get_pin(self):
        return self._pin

    def set_handler(self, handler):
        def _button_handler(p):
            handler(self)

        self._pin.irq(_button_handler)
