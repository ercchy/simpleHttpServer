HOST = ''
PORT = 5555

from http_server.server import run


if __name__ == '__main__':
    run(host=HOST, port=PORT)

