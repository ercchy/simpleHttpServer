"""
Client - Server application creatued using sockets lib

This is a Client side

author: The Ercchynator :)
"""
import socket
import sys

class Connection(object):
	
	def __init__(self, host, port):	
		super(Connection, self).__init__()
		self.host = host
		self.port = int(port)


def create_socket():
	# create an AF_INER, STREAM socket (TCP)
	#Adress family: AF_INET (IPv4)
	#Type: SOCK_STREAM (TCP protocol)
	try:
	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error, msg:
	    print 'Failed to create socket. Error code: ' + str(msg[0]) + ', Error message: ' + msg[1]
	    sys.exit()

	print 'Socket created'
	return s


def get_host_by_name(s, host):	
	try:
	    return socket.gethostbyname(host)
	except socket.gaierror:
	    print 'Hostname could not be resolved, Exiting...'
	    sys.exit()


def connect_to_host(conn):
	socket = create_socket()

	remote_ip = get_host_by_name(socket, conn.host)
	print 'IP address of ' + conn.host + ' is ' + remote_ip
	
	socket.connect((remote_ip, conn.port))

	print 'Socket Connected to ' + conn.host + ' on IP ' + remote_ip
	return socket


def send_data(s, msg):
	try:
		s.sendall(msg)
	except socket.error:
		print 
		sys.exit(1)	
	print 'Message sent successfully'


def recive_data(s):
	return s.recv(4096)


def main():
	if len(sys.argv) == 2:
		try:
			args = sys.argv[1].split(':')
			conn = Connection(args[0],  args[1])
		except Exception, e:
			print 'usage: ./client.py hostname:port'
			sys.exit(1)		
	elif len(sys.argv) == 1:
		conn = Connection('localhost', 8000)

	s = connect_to_host(conn)

	request = 'GET / HTTP/1.1\r\n\r\n'

	send_data(s, request)

	print recive_data(s)

	s.close()

if __name__ == '__main__':
  main()
