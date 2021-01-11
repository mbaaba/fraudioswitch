# ..............................................................................#
# the WebWatcher will be used, if we have a WebSocket-Server within the future  #
# ..............................................................................#


def _compute_line(button):
    # only dummy code
    print(button)
    line = 0
    return line


def watch(button, dispatch):
    return dispatch(_compute_line(button))
