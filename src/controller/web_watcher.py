def _compute_line(request):
    print(request)
    pos = request.find('/?line')
    line = 2  # MUTE ==> Stitch.MUTE
    if pos > 0:
        line = int(request[pos+7:pos+8])

    return line


def watch(request, dispatch):
    return dispatch(_compute_line(request))
