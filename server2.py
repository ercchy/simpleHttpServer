from socket import *
from http_protocol.request import parse_http_request

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
        print request
        msg_back = 'HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n<html><body>%s</body></html>' % request
        clientsock.send(msg_back)
        clientsock.close()

