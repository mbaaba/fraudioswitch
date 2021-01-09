try:
    import usocket as socket
except:
    import socket

from internet.web_site import web_page

connected_socket = None

def init_server():
    global connected_socket
    connected_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected_socket.bind(('', 80))
    connected_socket.listen(5)


#def _led_response(request, leds):
    # led_1 = request.find('/?led=1') == 6
    # led_2 = request.find('/?led=2') == 6
    # led_3 = request.find('/?led=3') == 6
    # led_4 = request.find('/?led=4') == 6
    #
    # leds[0].value(led_1)
    # leds[1].value(led_2)
    # leds[2].value(led_3)
    # leds[3].value(led_4)
    #
    # response = web_page("1")
    # return response


def _dispatch(request):
    response = web_page("1")
    print('Content ={}'.format(request))
    is_led = request.find('/?led') == 6

    if is_led:
        response = web_page("1")

    return response


def run_server(web_watch):
    conn, addr = connected_socket.accept()
    request = str(conn.recv(1024))
    web_watch(request)

    response = _dispatch(request)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
