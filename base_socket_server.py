"""
Simple Base server
"""
import sys
import socket
import select
from thread import start_new_thread


class BaseSocketServer:

    adress_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 10
    allow_reuse_address = False


    def __init__(self, server_address, bind_and_activate=True):
        self.server_address = server_address
        self.socket = socket.socket(self.adress_family,
                                    self.socket_type)
        print 'Socket created'
        if bind_and_activate:
            self.bind_server()
            self.server_activate()


    def bind_server(self):
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()
        print 'Socket binded, server address: %s on port %s' % (self.server_address[0], self.server_address[1])


    def server_activate(self):
        self.socket.listen(self.request_queue_size)
        print 'Socket listening'


    def server_close(self):
        self.socket.close()


    def get_request(self):
        self.socket.accept()


    def create_thread(self, request):
        while True:
            data = request.recv(1024)
            request.sendall('200 HTTP/1.0 %s' % data)


    def serve_forever(self):
        while True:
            try:
                request, client_address = self.socket.accept()
                start_new_thread(self.create_thread, (request,))
            except socket.error:
                return
            print request.type, client_address



def test(ServerClass = BaseSocketServer, protocol="HTTP/1.0"):

    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 8000
    server_address = ('', port)

    httpd = ServerClass(server_address)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()



if __name__=='__main__':
    test()

