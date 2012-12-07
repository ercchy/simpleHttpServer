import os
from socket import *
from file_server.helper import get_file
from http_protocol.request import parse_http_request
from http_protocol.response import HttpResponse
from http_protocol.response import render_http_response

CURRENT_DIR = os.path.dirname(__file__)

if __name__=='__main__':
    HOST = 'localhost'
    PORT = 5555
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.bind(ADDR)
    serversock.listen(2)
    while 1:
        print 'waiting for connection...'
        clientsock, addr = serversock.accept()
        print '...connected from:', addr
        data = clientsock.recv(BUFSIZ)
        request = parse_http_request(data)

        file = get_file(request.request_uri)

        if file.exists:
            response = HttpResponse(protocol=request.protocol, status_code=200)
            response.headers['Content-type'] = file.mime_type
            response.content = file.content
        else:
            response = HttpResponse(protocol=request.protocol, status_code=404)
            response.headers['Content-type'] = 'text/plain'
            response.content = 'This file does not exist!'
            
        response_msg = render_http_response(response)
        clientsock.send(response_msg)
        clientsock.close()

