from board import LED_23
from http_server import init_server, run_server
from web_site import web_page

s = init_server()

while True:
    run_server(s, LED_23, web_page)