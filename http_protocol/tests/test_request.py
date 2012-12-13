"""
My simple HTTP protocol parsing and handling.
"""
from nose import tools
from ..request import parse_http_request
from ..exceptions import HttpParseException


GOOD_REQUEST_1 = \
'''GET / HTTP/1.1
Host: localhost:5555
Connection: keep-alive
Cache-Control: max-age=0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.95 Safari/537.11
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate,sdch
Accept-Language: en-US,en;q=0.8
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3'''

GOOD_REQUEST_2 = \
'''GET / HTTP/1.1'''

BAD_REQUEST_1 = \
'''
NOT_REAllz httP
'''

BAD_REQUEST_2 = \
'''GET / HTTP/1.1
Host; localhost:5555
'''

REQUEST_WITH_RANGE_FROM_ZERO = \
'''GET /test_1.txt HTTP/1.1
Host: localhost:5555
Range: bytes=0-'''

REQUEST_WITH_RANGE_FROM_MIDDLE =\
'''GET /test_1.txt HTTP/1.1
Host: localhost:5555
Range: bytes=5-10'''


def test_good_http_request_1():
    # setup
    headers_expected_result = {
        'Host': 'localhost:5555',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.95 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    }

    # run
    http_request = parse_http_request(GOOD_REQUEST_1)

    # assert
    tools.assert_equals(http_request.method, 'GET')
    tools.assert_equals(http_request.request_uri, '/')
    tools.assert_equals(http_request.protocol, 'HTTP/1.1')
    tools.assert_equals(http_request.headers, headers_expected_result)


def test_good_http_request_2():
    # setup
    headers_expected_result = {}

    # run
    http_request = parse_http_request(GOOD_REQUEST_2)

    # assert
    tools.assert_equals(http_request.method, 'GET')
    tools.assert_equals(http_request.request_uri, '/')
    tools.assert_equals(http_request.protocol, 'HTTP/1.1')
    tools.assert_equals(http_request.headers, headers_expected_result)


@tools.raises(HttpParseException)
def test_http_request_data_none():
    parse_http_request(None)


@tools.raises(HttpParseException)
def test_http_request_data_empty_string():
    parse_http_request('')


@tools.raises(HttpParseException)
def test_bad_http_request_1():
    parse_http_request(BAD_REQUEST_1)


@tools.raises(HttpParseException)
def test_bad_http_request_2():
    parse_http_request(BAD_REQUEST_2)


def test_request_parsing_with_range_from_zero():
    # run
    http_request = parse_http_request(REQUEST_WITH_RANGE_FROM_ZERO)

    # assert
    tools.assert_true(http_request.is_range_requested())
    tools.assert_equals(http_request.get_range(), (0, None))


def test_request_parsing_with_range_from_middle():
    # run
    http_request = parse_http_request(REQUEST_WITH_RANGE_FROM_MIDDLE)

    # assert
    tools.assert_true(http_request.is_range_requested())
    tools.assert_equals(http_request.get_range(), (5, 10))
