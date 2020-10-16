from datetime import datetime

import http.server
import socketserver
import cgi


LISTEN_PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler


def main():

    with socketserver.TCPServer(("", LISTEN_PORT), ServerHandler) as server:
        try:
            # Listen for requests indefinitely
            server.serve_forever()
        except KeyboardInterrupt:
            # A request to terminate has been received, stop the server
            print("\nShutting down...")
            server.socket.close()


class ServerHandler(Handler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # self.wfile.write(b"<h1>It works!</h1>")


if __name__ == "__main__":
    main()