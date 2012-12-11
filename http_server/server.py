from socket import *
import thread
from file_system.helper import get_file
from http_protocol.request import parse_http_request
from http_protocol.response import HttpResponse

BUFSIZ = 1024

def handle_request(clientsock):

    data = clientsock.recv(BUFSIZ)
    print 'Request: ', data
    request = parse_http_request(data)

    file = get_file(request.request_uri)

    if file.exists:
        if 'Range' in request.headers:
            response = HttpResponse(protocol=request.protocol, status_code=206,
                content_range=request.headers['Range'])
        else:
            response = HttpResponse(protocol=request.protocol, status_code=200)
        response.file = file
    else:
        response = HttpResponse(protocol=request.protocol, status_code=404)
        response.headers['Content-type'] = 'text/plain'
        response.content = 'This file does not exist!'

    response.write_to(clientsock)
    clientsock.close()


def run(host, port):

    address = (host, port)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.bind(address)
    serversock.listen(2)

    while 1:
        print 'waiting for connection...'
        clientsock, addr = serversock.accept()
        print '...connected from:', addr

        thread.start_new_thread(handle_request, (clientsock,))


