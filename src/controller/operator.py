from switch.switch import Switch

mySwitch = Switch()


def watch_web(request):
    line_1 = request.find('/?led=1') == 6
    line_2 = request.find('/?led=2') == 6
    line_3 = request.find('/?led=3') == 6

    if line_1:
        mySwitch.activate(1)
    elif line_2:
        mySwitch.activate(2)
    elif line_3:
        mySwitch.activate(3)
    else:
        mySwitch.activate(0)

