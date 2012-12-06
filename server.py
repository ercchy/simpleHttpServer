"""
Client - Server application creatued using sockets lib

This is a Server side

author: The Ercchynator :)
"""
import socket
import sys
from Queue import Queue
from threading import Thread
from SimpleHTTPServer import SimpleHTTPRequestHandler

"""
def bind_socket(s, host_data):

	try:
		s.bind((host_data.host, host_data.port))
		print 'Socket bind complete'
		return s
	except socket.error , msg:
		s.close()
		print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message: ' + msg[1]
        sys.exit()


def open_thread(conn):
	
	data = None
	while True:
		try:
			data = conn.recv(1024)
			reply = 'HTTP/1.0 200 OK\r\nContent-Type:text/html\r\nConnection:keep-alive\r\n\r\n<html><head>foo</head></html>\r\n'
			print data
		except Error as e:
			print 'Connection is not working dammit' + e

		
		if not data:
			break

		conn.sendall(reply)

	conn.close()

"""
class BaseServer:
    # create an AF_INER, STREAM socket (TCP)
    # Adress family: AF_INET (IPv4)
    # Type: SOCK_STREAM (TCP protocol)
    adress_family = socket.AF_INET

    socket_type = socket.SOCK_STREAM

    request_queue_size = 10

    def __init__(self, server_address, bind_and_activate=True):
        self.socket = socket.socket(self.adress_family, self.socket_type)
        self.server_address = server_address

        if bind_and_activate:
            self.server_bind()
            self.server_activate()


    def server_bind(self):
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()


    def server_activate(self):
        self.socket.listen(self.request_queue_size)


    def server_close(self):
        self.socket.close()


    def serve_forever(self, threadpool):
        while True:
            conn, addr = self.socket.accept()
            print 'Connected with ' + addr[0] + ':' + str(addr[1])




class Worker(Thread):
    """Thread executing tasks from a given tasks queue"""
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try: func(*args, **kargs)
            except Exception, e: print e
            self.tasks.task_done()


class ThreadPool:
    """Pool of threads consuming tasks from a queue"""
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads): Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """Add a task to the queue"""
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        """Wait for completion of all the tasks in the queue"""
        self.tasks.join()


class BasicHTTPThreadingServer(ThreadPool, BaseServer):

    def server_bind(self):
        BaseServer.server_bind(self)

        host, port = self.socket.getsockname()[:2]
        print host
        self.server_name = socket.getfqdn(host)
        self.server_port = port
        self.pool = ThreadPool(20)


    def serve_forever(self, threadpool):
        while True:
            conn, addr = self.socket.accept()
            print 'Connected with ' + addr[0] + ':' + str(addr[1])
            #self.pool.add_task(conn)


        """
        try:
            s.bind((host_data.host, host_data.port))
            print 'Socket bind complete'
            return s
        except socket.error , msg:
            s.close()
            print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message: ' + msg[1]
        sys.exit()
        """



def test():
    if sys.argv[1:]:
        port = sys.argv[1]
    else:
        port = 8000

    server_address = ('', port)
    try:
        httpd = BasicHTTPThreadingServer(server_address)
        sa = httpd.socket.getsockname()
        print "Serving HTTP on", sa[0], "port", sa[1], "..."
        #httpd.serve_forever(httpd.pool)
    except KeyboardInterrupt:
        httpd.server_close()



    """
	s = bind_socket(create_socket(), host_data)

	s.listen(10)
	print 'Socket is now listening'
    """
    """
	while True:
		conn, addr = s.accept()
		print 'Content with ' + addr[0] + ': ' + str(addr[1])
		start_new_thread(open_thread,(conn,))
	
	s.close()
    """


if __name__ == '__main__':
    test()

"""
import SocketServer

class BaseHTTPMultiThreadServer(SocketServer.ThreadingTCPServer):

    def server_bind(self):
        SocketServer.ThreadingTCPServer.server_bind(self)
        host, port = self.socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port


class BaseRequestHandler:
    pass


def test():
    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 8000
    server_address = ('', port)

    httpd = BaseHTTPMultiThreadServer(server_address, BaseRequestHandler)
    sa = httpd.socket.getsockname()

    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()

if __name__ == '__main__':
    test()
"""