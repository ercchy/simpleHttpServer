"""
My simple file server handling.
"""
from nose import tools
from helper import get_file


def test_get_file_1():
    file = get_file('/test_1.txt')


    tools.assert_equals(file.exists, True)
    tools.assert_equals(file.mime_type, 'text/plain')


