"""
Client - Server application creatued using sockets lib

This is a Client side

author: The Ercchynator :)
"""
import socket
import sys

# create an AF_INER, STREAM socket (TCP)
#Adress family: AF_INET (IPv4)
#Type: SOCK_STREAM (TCP protocol)


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ', Error message: ' + msg[1]
    sys.exit()

print 'Socket created'


host = 'www.google.com'
port = 80

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print 'Hostname could not be resolved, Exiting...'
    sys.exit()

print 'IP address of ' + host + ' is ' + remote_ip

s.connect((remote_ip, port))

print 'Socket Connected to ' + host + ' on IP ' + remote_ip

message = 'GET / HTTP/1.1\r\n\r\n'

try:
    s.sendall(message)
except socket.error:
    print 'Sending failed. Exiting ...'
    sys.exit()
print 'Message sent successfully'

reply = s.recv(4096)

print reply

s.close()
