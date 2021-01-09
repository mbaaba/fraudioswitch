from internet.http_server import init_server, run_server
from controller.operator import watch_web

init_server()

while True:
    run_server(watch_web)