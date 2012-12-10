"""
My simple HTTP protocol parsing and handling.
"""
from nose import tools
from http_server.mock_client_socket import MockClientSocket
from http_server.server import handle_request


HTTP_REQUEST_UNKNOWN_FILE = \
'''GET /test_1.xxx HTTP/1.1
Host: localhost:5555'''

HTTP_RESPONSE_UNKNOWN_FILE = \
'''HTTP/1.1 404 Not Found
Content-type: text/plain

This file does not exist!'''

HTTP_REQUEST_KNOWN_FILE = \
'''GET /test_1.txt HTTP/1.1
Host: localhost:5555'''

HTTP_RESPONSE_KNOWN_FILE =\
'''HTTP/1.1 200 OK
Content-Length: 16
Content-type: text/plain

This is a test 1'''


def test_handle_request_unknown_file():
    #setup
    clientsock = MockClientSocket(recv_data=HTTP_REQUEST_UNKNOWN_FILE)

    #run
    handle_request(clientsock)

    # assert
    tools.assert_equals(clientsock.close_called, True)
    tools.assert_equals(clientsock.sent_data, HTTP_RESPONSE_UNKNOWN_FILE)


def test_handle_request_known_file():
    #setup
    clientsock = MockClientSocket(recv_data=HTTP_REQUEST_KNOWN_FILE)

    #run
    handle_request(clientsock)

    # assert
    tools.assert_equals(clientsock.close_called, True)
    tools.assert_equals(clientsock.sent_data, HTTP_RESPONSE_KNOWN_FILE)











