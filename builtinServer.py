import SocketServer
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler



class CustomHTTPThreadingServer(SocketServer.ThreadingTCPServer, HTTPServer):
    """
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		self.wfile.write('<HTML><body>Hello World!</body></HTML>')
		return
    """
    pass


def main():
    try:
        server = CustomHTTPThreadingServer(('', 8000), SimpleHTTPRequestHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()


if __name__ == '__main__':
    main()