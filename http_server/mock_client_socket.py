

class MockClientSocket(object):
    def __init__(self, recv_data=None):
        self.sent_data = ''
        self.recv_data = recv_data
        self.close_called = False


    def sendall(self, data):
        self.sent_data += data


    def recv(self, buffer_size):
        return self.recv_data


    def close(self):
        self.close_called = True
