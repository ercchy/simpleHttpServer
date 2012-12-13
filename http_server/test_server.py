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

HTTP_RESPONSE_KNOWN_FILE = \
'''HTTP/1.1 200 OK
Content-Length: 16
Content-type: text/plain
Accept-Ranges: bytes

This is a test 1'''

HTTP_REQUEST_RANGE_FROM_ZERO = \
'''GET /test_1.txt HTTP/1.1
Host: localhost:5555
Range: bytes=0-'''

HTTP_RESPONSE_RANGE_FROM_ZERO = \
'''HTTP/1.1 206 Partial Content
Content-Length: 16
Content-type: text/plain
Accept-Ranges: bytes
Content-Range: bytes 0-15/16

This is a test 1'''

HTTP_REQUEST_RANGE_FROM_MIDDLE = \
'''GET /test_1.txt HTTP/1.1
Host: localhost:5555
Range: bytes=5-'''

HTTP_RESPONSE_RANGE_FROM_MIDDLE = \
'''HTTP/1.1 206 Partial Content
Content-Length: 11
Content-type: text/plain
Accept-Ranges: bytes
Content-Range: bytes 5-15/16

is a test 1'''

# Add another request response for 5-10/16 range


def test_handle_request_unknown_file():
    # setup
    clientsock = MockClientSocket(recv_data=HTTP_REQUEST_UNKNOWN_FILE)

    # run
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


def test_handle_request_range_from_zero():
    # setup
    clientsock = MockClientSocket(recv_data=HTTP_REQUEST_RANGE_FROM_ZERO)

    # run
    handle_request(clientsock)

    # assert
    tools.assert_equals(clientsock.sent_data, HTTP_RESPONSE_RANGE_FROM_ZERO)


def test_handle_request_range_from_middle():
    # setup
    clientsock = MockClientSocket(recv_data=HTTP_REQUEST_RANGE_FROM_MIDDLE)

    # run
    handle_request(clientsock)

    # assert
    tools.assert_equals(clientsock.sent_data, HTTP_RESPONSE_RANGE_FROM_MIDDLE)












