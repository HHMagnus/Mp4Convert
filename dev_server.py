# save as dev_server.py
from http.server import SimpleHTTPRequestHandler, HTTPServer

class COIServerHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers for cross-origin isolation
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

if __name__ == "__main__":
    port = 8000
    server = HTTPServer(("localhost", port), COIServerHandler)
    print(f"Serving on http://localhost:{port}")
    server.serve_forever()
