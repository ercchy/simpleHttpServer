"""
File system helper tests.
"""
from nose import tools
from helper import get_file
from http_server.mock_client_socket import MockClientSocket

FILE = '/test_1.txt'

HTTP_REQUEST_KNOWN_FILE = \
'''GET /test_1.txt HTTP/1.1
Host: localhost:5555'''


def test_get_file_1():
    file = get_file(FILE)

    tools.assert_equals(file.exists, True)
    tools.assert_equals(file.mime_type, 'text/plain')


def test_stream_whole_file():
    # setup
    file = get_file(FILE)
    range = (0, file.file_size - 1)
    clientsock = MockClientSocket(recv_data=HTTP_REQUEST_KNOWN_FILE)

    # run
    file.stream_to(clientsock, range, file_chunk_size=1)

    # assert
    tools.assert_equals(clientsock.sent_data, 'This is a test 1')


def test_stream_middle_part_of_file():
    # setup
    file = get_file(FILE)
    range = (5, 10)
    clientsock = MockClientSocket(recv_data=HTTP_REQUEST_KNOWN_FILE)

    # run
    file.stream_to(clientsock, range, file_chunk_size=None)

    # assert
    tools.assert_equals(clientsock.sent_data, 'is a t')


def test_stream_end_part_of_file():
    # setup
    file = get_file(FILE)
    range = (10, file.file_size - 1)
    clientsock = MockClientSocket(recv_data=HTTP_REQUEST_KNOWN_FILE)

    # run
    file.stream_to(clientsock, range, file_chunk_size=None)

    # assert
    tools.assert_equals(clientsock.sent_data, 'test 1')
