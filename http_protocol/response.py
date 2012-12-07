"""
My simple HTTP protocol parsing and handling.
"""
from status_codes import HTTP_STATUS_CODES


class HttpResponse(object):


    def __init__(self, protocol, status_code):
        assert status_code in HTTP_STATUS_CODES, 'Unknown status code.'

        self.protocol = protocol
        self.status_code = status_code
        self.headers = {}
        self.content = ''

    def __str__(self):
        return 'HttpRequest (protocol=%s, status_code=%s)' % \
               (self.protocol, self.status_code)


def render_http_response(response):
    ret_val = []

    response_line = '%s %s %s' % (response.protocol, response.status_code,
                                  HTTP_STATUS_CODES[response.status_code][0])

    ret_val.append(response_line)

    for key, value in response.headers.iteritems():
        header_line = '%s: %s' % (key, value)
        ret_val.append(header_line)

    ret_val.append('')
    ret_val.append(response.content)

    return '\n'.join(ret_val)
