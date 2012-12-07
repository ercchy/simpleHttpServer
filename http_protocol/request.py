"""
My simple HTTP protocol parsing and handling.
"""

from exceptions import HttpParseException


class HttpRequest(object):
    def __init__(self, method, request_uri, protocol, headers):
        self.method = method
        self.request_uri = request_uri
        self.protocol = protocol
        self.headers = headers

    def __str__(self):
        return 'HttpRequest (method=%s, request_uri=%s, protocol=%s)' % (self.method, self.request_uri, self.protocol)


def parse_http_request(data):
    # guard, check input parameters
    if not data:
        raise HttpParseException('Input parameter data must be provided.')

    data_lines = data.splitlines(False)

    request_cmpts = data_lines[0].split(' ')

    if len(request_cmpts) != 3:
        raise HttpParseException('Cannot parse HTTP request line: %s' % data_lines[0])

    method, request_uri, protocol = request_cmpts[0], request_cmpts[1], request_cmpts[2]

    headers = {}
    for line in data_lines[1:]:
        if not line:
            continue

        line_cmpts = line.split(': ')

        if len(line_cmpts) != 2:
            raise HttpParseException('Cannot parse HTTP header line: %s' % line)

        key, value = line_cmpts[0], line_cmpts[1]
        headers[key] = value

    return HttpRequest(method, request_uri, protocol, headers)
