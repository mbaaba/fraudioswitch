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


def _dispatch(request, web_watch):
    response = web_page("0")
    print('Content ={}'.format(request))
    is_led = request.find('/?led') == 6

    if is_led:
        response = web_page(str(web_watch(request)))

    return response


def run_server(web_watch):
    conn, addr = connected_socket.accept()
    request = str(conn.recv(1024))
    response = _dispatch(request, web_watch)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
