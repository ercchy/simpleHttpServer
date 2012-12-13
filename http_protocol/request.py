"""
HTTP request.
"""

import re
import logging
from exceptions import HttpParseException

Log = logging.getLogger('simpleHttpServer.server')


class HttpRequest(object):
    def __init__(self, method, request_uri, protocol, headers):
        self.method = method
        self.request_uri = request_uri
        self.protocol = protocol
        self.headers = headers

    def __str__(self):
        return 'HttpRequest (method=%s, request_uri=%s, protocol=%s)' % \
               (self.method, self.request_uri, self.protocol)

    def is_range_requested(self):
        return 'Range' in self.headers

    def get_range(self):
        range_header_value = None

        if self.is_range_requested():
            range_header_value = self.headers['Range']

        if range_header_value:
            range_start, range_end = None, None

            range = re.findall(r'\d+', range_header_value)
            range_start = int(range[0])

            if len(range) > 1:
                range_end = int(range[1])

            return range_start, range_end

        return None, None


def parse_http_request(data):
    # guard, check input parameters
    if not data:
        error = 'Input parameter data must be provided.'
        Log.error(error)
        raise HttpParseException(error)

    data_lines = data.splitlines(False)

    request_line = data_lines[0]
    request_cmpts = request_line.split(' ')

    if len(request_cmpts) != 3:
        error = 'Cannot parse HTTP request line: %s' % request_line
        Log.error(error)
        raise HttpParseException(error)

    method, request_uri, protocol = request_cmpts[0], request_cmpts[1], request_cmpts[2]
    headers = {}

    for line in data_lines[1:]:
        if not line:
            break

        line_cmpts = line.split(': ')

        if len(line_cmpts) != 2:
            raise HttpParseException('Cannot parse HTTP header line: %s' % line)

        key, value = line_cmpts[0], line_cmpts[1]
        headers[key] = value

    return HttpRequest(method, request_uri, protocol, headers)
