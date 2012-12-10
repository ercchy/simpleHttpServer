import os
import mimetypes
from config import STATIC_FILES_DIR

class File(object):
    def __init__(self, request_uri=None, file_name=None, file_size=None, exists=False, mime_type=None):
        self.request_uri = request_uri
        self.file_name = file_name
        self.file_size = file_size
        self.exists = exists
        self.mime_type = mime_type


    def __str__(self):
        return 'File (request_uri=%s, file_name=%s, exists=%s, mime_type=%s)' % \
               (self.request_uri, self.file_name, self.exists, self.mime_type)


    def open(self):
        return open(self.file_name, 'rb')


def get_file(request_uri):
    fn = STATIC_FILES_DIR + request_uri
    fsize = None
    exists = False
    mime_type = ''

    try:
        fsize = os.path.getsize(fn)
        exists = True
        type, encoding = mimetypes.guess_type(request_uri)
        if type:
            mime_type = type
    except:
        pass

    return File(request_uri, fn, fsize, exists, mime_type)
