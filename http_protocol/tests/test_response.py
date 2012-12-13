"""
My simple HTTP protocol parsing and handling.
"""
from nose import tools
from http_server.mock_client_socket import MockClientSocket
from ..response import HttpResponse


def test_simple_response():
    #setup
    response = HttpResponse(protocol='HTTP/1.1', status_code=200)
    response.headers['Date'] = 'Fri, 31 Dec 1999 23:59:59 GMT'
    response.headers['Content-type'] = 'text/plain'
    response.content = 'This is a test'

    expected_response_msg = \
    '''HTTP/1.1 200 OK
Date: Fri, 31 Dec 1999 23:59:59 GMT
Content-type: text/plain

This is a test'''

    #run
    clientsock = MockClientSocket()
    response.write_to(clientsock)

    #assert
    tools.assert_equals(clientsock.sent_data, expected_response_msg)
