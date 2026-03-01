#!/usr/bin/env python3
"""
Simple API server to demonstrate nginx proxy_pass.
Run on port 5000, nginx will proxy requests from port 8000 to it.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import datetime


class APIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/status":
            body = json.dumps({
                "status": "ok",
                "time": datetime.datetime.now().isoformat(),
                "message": "Hello from the backend API!"
            }).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"error": "not found"}')

    def log_message(self, fmt, *args):
        print(f"[API] {self.address_string()} - {fmt % args}")


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 5000), APIHandler)
    print("API server running on http://127.0.0.1:5000")
    server.serve_forever()
