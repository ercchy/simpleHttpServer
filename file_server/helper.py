import mimetypes

class File(object):
    def __init__(self, request_uri=None, exists=False, mime_type=None, content=None):
        self.request_uri = request_uri
        self.exists = exists
        self.mime_type = mime_type
        self.content = content

    def __str__(self):
        return 'File (request_uri=%s, exists=%s, mime_type=%s)' % (self.request_uri, self.exists, self.mime_type)


def get_file(request_uri):
    fn = '/home/erika/DEV/ercchy/simpleHttpServer/static_files' + request_uri
    exists = False
    content = ''
    mime_type = ''

    try:
        with open(fn, 'r') as f:
            content = f.read()
        exists = True
        type, encoding = mimetypes.guess_type(request_uri)
        if type:
            mime_type = type
    except:
        pass

    return File(request_uri, exists, mime_type, content)
