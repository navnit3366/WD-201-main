from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime


class MyServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()

        # print the current path
        # as it an attribute of the SimpleHTTPRequestHandler Class
        # print(self.path)
        if self.path == "/hello":
            content = f"<h1>Hello, world! {datetime.now()} </h1>"
        else:
            content = "<h1>Error!</h1>"

        self.wfile.write(content.encode())


address = "127.0.0.1"
port = 8000
server_address = (address, port)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()
