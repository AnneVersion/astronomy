"""Astronomy App - port 8765"""
import http.server
import os

PORT = 8765
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class CORSHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

print(f"Astronomy app: http://localhost:{PORT}")
http.server.ThreadingHTTPServer(('', PORT), CORSHandler).serve_forever()
