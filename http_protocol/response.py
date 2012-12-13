"""
My simple HTTP protocol parsing and handling.
"""
import logging
from status_codes import HTTP_STATUS_CODES


Log = logging.getLogger('simpleHttpServer.response')

class HttpResponse(object):


    def __init__(self, protocol, status_code, range=None):
        assert status_code in HTTP_STATUS_CODES, 'Unknown status code.'

        self.protocol = protocol
        self.status_code = status_code
        self.headers = {}
        self.range = range
        self.content = ''
        self.file = None


    def __str__(self):
        return 'HttpRequest (protocol=%s, status_code=%s)' % \
               (self.protocol, self.status_code)


    def write_to(self, output):

        if self.file:
            self.headers['Content-type'] = self.file.mime_type
            self.headers['Content-Length'] = self.file.file_size
            self.headers['Accept-Ranges'] = 'bytes'

            if self.range:
                range_start, range_end = self.file.calculate_range(self.range)

                self.headers['Content-Range'] = 'bytes %s-%s/%s' % (range_start, range_end,
                                                                    self.file.file_size)
                self.headers['Content-Length'] = range_end - range_start + 1

        response_msg = render_http_response(self)

        output.sendall(response_msg)

        Log.debug('Response:\n%s', response_msg)

        if self.file:
            self.file.stream_to(output, range=self.file.calculate_range(self.range))




def render_http_response(response):
    ret_val = []

    response_line = '%s %s %s' % (response.protocol, response.status_code,
                                  HTTP_STATUS_CODES[response.status_code][0])

    ret_val.append(response_line)

    for key, value in response.headers.iteritems():
        header_line = '%s: %s' % (key, value)
        ret_val.append(header_line)

    ret_val.append('')

    if response.content:
        ret_val.append(response.content)
    else:
        ret_val.append('')

    return '\n'.join(ret_val)
