from switch.switch import Switch
from controller.web_watcher import watch as web_watch

audio_switch = Switch()


def watch_web():
    def f(request):
        return web_watch(request, dispatch_web)

    return f


def dispatch_web(line):
    audio_switch.activate(line)
    return audio_switch.get_active_line()
