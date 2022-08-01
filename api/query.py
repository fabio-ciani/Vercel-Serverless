from http.server import BaseHTTPRequestHandler
from urllib.parse import *
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        query = dict(parse_qsl(urlparse(self.path).query))
        self.wfile.write(json.dumps(query, indent = 4).encode())
        return
