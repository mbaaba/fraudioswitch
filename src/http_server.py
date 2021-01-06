try:
    import usocket as socket
except:
    import socket


def init_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    return s


def _led_response(request, led, web_page):
    led_on = request.find('/?led=on')
    led_off = request.find('/?led=off')

    if led_on == 6:
        print('LED ON')
        led.value(1)
    if led_off == 6:
        print('LED OFF')
        led.value(0)

    response = web_page(led)
    return response


def _dispatch(request, led, web_page):
    request = str(request)
    response = web_page(led)
    print('Content ={}'.format(request))
    is_led = request.find('/?led') == 6

    if is_led:
        response = _led_response(request, led, web_page)

    return response


def run_server(sock, led, web_page):
    conn, addr = sock.accept()
    request = conn.recv(1024)

    response = _dispatch(request, led, web_page)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
