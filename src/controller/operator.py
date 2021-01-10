from switch.switch import Switch
from controller.web_watcher import watch as web_watch

audio_switch = Switch()


def watch_web():
    def f(request):
        return web_watch(request, dispatch_web)

    return f


def dispatch_web(web_event):
    audio_switch.activate(web_event.get_line())
    return audio_switch.get_active_line()
