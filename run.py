import logging
from http_server.server import run
from config import HOST
from config import PORT
from config import setup_logging


if __name__ == '__main__':
    setup_logging()

    Log = logging.getLogger('simpleHttpServer.run')

    try:
        run(host=HOST, port=PORT)
    except KeyboardInterrupt:
        Log.info('Server stopped')

