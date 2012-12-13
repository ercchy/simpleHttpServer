"""
Helper method for File class
"""
import os
import logging
import mimetypes
import socket
from config import STATIC_FILES_DIR
from config import FILE_CHUNK_SIZE

Log = logging.getLogger('simpleHttpServer.helper')


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

    def calculate_range(self, range):
        range_start, range_end = 0, None

        if range:
            range_start, range_end = range

        if not range_end:
            range_end = self.file_size - 1

        return range_start, range_end

    def stream_to(self, output, range, file_chunk_size=None):

        if not file_chunk_size:
            file_chunk_size = FILE_CHUNK_SIZE

        range_start, range_end = range

        with self.open() as f:
            f.seek(range_start)
            remaining_bytes = range_end - range_start + 1

            while remaining_bytes > 0:
                bytes_read = f.read(min(remaining_bytes, file_chunk_size))
                try:
                    output.sendall(bytes_read)
                except socket.error, (val, msg):
                    if val == 104:
                        Log.debug('Error occured: %s %s', val, msg)
                        pass
                remaining_bytes -= file_chunk_size


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
