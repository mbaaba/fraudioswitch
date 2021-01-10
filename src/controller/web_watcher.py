from controller.web_event import WebEvent


def _compute_line(request):
    print(request)
    pos = request.find('/?led')
    line = 0
    if pos > 0:
        line = int(request[pos+6:pos+7])

    return line


def _create_event(request):
    return WebEvent(request, _compute_line(request))


def watch(request, dispatch):
    return dispatch(_create_event(request))
