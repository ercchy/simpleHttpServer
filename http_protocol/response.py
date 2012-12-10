"""
My simple HTTP protocol parsing and handling.
"""
from status_codes import HTTP_STATUS_CODES

FILE_CHUNK_SIZE = 1024 * 1024 #4 * 1024 # 4 kilobytes


class HttpResponse(object):


    def __init__(self, protocol, status_code):
        assert status_code in HTTP_STATUS_CODES, 'Unknown status code.'

        self.protocol = protocol
        self.status_code = status_code
        self.headers = {}
        self.content = ''
        self.file = None


    def __str__(self):
        return 'HttpRequest (protocol=%s, status_code=%s)' % \
               (self.protocol, self.status_code)


    def write_to(self, output):

        if self.file:
            self.headers['Content-type'] = self.file.mime_type
            self.headers['Content-Length'] = self.file.file_size

        response_msg = render_http_response(self)
        output.send(response_msg)

        if self.file:
            position = 0
            with self.file.open() as f:
                bytes_read = f.read(FILE_CHUNK_SIZE)
                while bytes_read != '':
                    print 'position: ', position
                    position += FILE_CHUNK_SIZE
                    output.send(bytes_read)
                    bytes_read = f.read(FILE_CHUNK_SIZE)


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
