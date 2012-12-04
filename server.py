"""
Client - Server application creatued using sockets lib

This is a Server side

author: The Ercchynator :)
"""
import socket
import sys
from thread import *

class HostData(object):
	
	def __init__(self, port):	
		super(HostData, self).__init__()
		self.host = ''
		self.port = int(port)


def create_socket():
	# create an AF_INER, STREAM socket (TCP)
	# Adress family: AF_INET (IPv4)
	# Type: SOCK_STREAM (TCP protocol)
	try:
	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error, msg:
	    print 'Failed to create socket. Error code: ' + str(msg[0]) + ', Error message: ' + msg[1]
	    sys.exit()

	print 'Socket created'
	return s


def bind_socket(s, host_data):

	try:
		s.bind((host_data.host, host_data.port))
		print 'Socket bind complete'
		return s
	except socket.error , msg:
		print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message: ' + msg[1]
        sys.exit()


def open_thread(conn):
	conn.send('Welocme to the server. Type something and then hit enter\n')

	while True:
		data = conn.recv(1024)
		reply = 'OK...' + data
		if not data:
			break

		conn.sendall(reply)
	conn.close()



def main():
	if len(sys.argv) == 2:
		try:
			args = sys.argv[1].split(':')			
			host_data = HostData(args[1])
		except Exception, e:
			print 'usage: ./client.py :port'
			sys.exit(1)		
	elif len(sys.argv) == 1:
		host_data = HostData(8000)

	s = bind_socket(create_socket(), host_data)

	s.listen(10)
	print 'Socket is now listening'

	while True:
		conn, addr = s.accept()
		print 'Content with ' + addr[0] + ': ' + str(addr[1])
		start_new_thread(open_thread,(conn,))
	
	s.close()



if __name__ == '__main__':
  main()
