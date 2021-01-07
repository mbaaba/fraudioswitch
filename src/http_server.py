try:
    import usocket as socket
except:
    import socket


def init_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    return s


def _led_response(request, leds, web_page):
    led_1 = request.find('/?led=1') == 6
    led_2 = request.find('/?led=2') == 6
    led_3 = request.find('/?led=3') == 6
    led_4 = request.find('/?led=4') == 6

    leds[0].value(led_1)
    leds[1].value(led_2)
    leds[2].value(led_3)
    leds[3].value(led_4)

    response = web_page("1")
    return response


def _dispatch(request, pins, web_page):
    request = str(request)
    response = web_page("1")
    print('Content ={}'.format(request))
    is_led = request.find('/?led') == 6

    if is_led:
        response = _led_response(request, pins, web_page)

    return response


def run_server(sock, pins, web_page):
    conn, addr = sock.accept()
    request = conn.recv(1024)

    response = _dispatch(request, pins, web_page)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
