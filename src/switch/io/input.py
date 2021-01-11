class Input:
    def __init__(self, pins, config):
        self._pins = pins
        self._config = config

    def activate(self):
        self._pins[0].value(self._config[0])
        self._pins[1].value(self._config[1])
