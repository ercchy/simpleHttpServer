import logging
import socket
from file_system.helper import get_file
from http_protocol.request import parse_http_request
from http_protocol.response import HttpResponse
from http_server.thread_pool import ThreadPool

Log = logging.getLogger('simpleHttpServer.server')

BUFSIZ = 1024

def handle_request(clientsock):

    data = clientsock.recv(BUFSIZ)

    Log.debug('Request received:\n%s', data)

    request = parse_http_request(data)

    file = get_file(request.request_uri)

    if file.exists:

        if request.is_range_requested():

            response = HttpResponse(protocol=request.protocol,
                status_code=206, range=request.get_range())
        else:
            response = HttpResponse(protocol=request.protocol, status_code=200)

        response.file = file
    else:
        response = HttpResponse(protocol=request.protocol, status_code=404)
        response.headers['Content-type'] = 'text/plain'
        response.content = 'This file does not exist!'

    Log.info('GET %s %s %s %s',
        request.request_uri, request.protocol, request.get_range(), response.status_code)

    response.write_to(clientsock)
    clientsock.close()


def run(host, port):

    address = (host, port)
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversock.bind(address)
    serversock.listen(2)

    Log.info('Server started...')

    pool = ThreadPool(3)

    while 1:
        Log.debug('Waiting for connection...')

        clientsock, addr = serversock.accept()
        Log.debug('Connected from: %s', addr)

        pool.add_task(handle_request, clientsock)

    pool.wait_completion()