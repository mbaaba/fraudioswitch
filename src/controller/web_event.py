class WebEvent:

    def __init__(self, request, line):
        self._request = request
        self._line = line

    def get_line(self):
        return self._line

    def get_request(self):
        return self._request