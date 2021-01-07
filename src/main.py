from board import PIN_19, PIN_21, PIN_22, PIN_23
from http_server import init_server, run_server
from web_site import web_page

s = init_server()
pins = [PIN_19, PIN_21, PIN_22, PIN_23]
while True:
    run_server(s, pins, web_page)