# loot.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("\n=== FLAG MASUK ===")
        print(self.path)
        print("=====================")
        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    print("LOOT SERVER RUNNING http://127.0.0.1:4444")
    HTTPServer(("0.0.0.0", 4444), Handler).serve_forever()
