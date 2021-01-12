class Input:
    WIRE_1 = 0
    WIRE_2 = 1
    WIRE_3 = 2

    def __init__(self, pins, config):
        self._pins = pins
        self._config = config

    def activate(self):
        self._pins[Input.WIRE_1].value(self._config[Input.WIRE_1])
        self._pins[Input.WIRE_2].value(self._config[Input.WIRE_2])
        self._pins[Input.WIRE_3].value(self._config[Input.WIRE_3])
