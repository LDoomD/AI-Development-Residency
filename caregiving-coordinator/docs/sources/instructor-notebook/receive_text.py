"""Local receiver: writes one POSTed text body to the file given in the X-Name header (127.0.0.1 only), then exits."""
import http.server, pathlib
OUT = pathlib.Path(__file__).parent
class H(http.server.BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*"); self.send_header("Access-Control-Allow-Headers", "*"); self.send_header("Access-Control-Allow-Private-Network", "true")
    def do_OPTIONS(self): self.send_response(204); self._cors(); self.end_headers()
    def do_POST(self):
        n = int(self.headers["Content-Length"]); body = self.rfile.read(n)
        name = pathlib.Path(self.headers.get("X-Name", "out.txt")).name
        (OUT / name).write_bytes(body); self.send_response(200); self._cors(); self.end_headers(); self.wfile.write(b"ok")
        print("saved", name, n, flush=True)
    def log_message(self, *a): pass
http.server.HTTPServer(("127.0.0.1", 8765), H).serve_forever()
