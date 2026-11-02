"""Tiny local receiver (127.0.0.1 only) so a browser page can hand review text to a script that writes the exact bytes.
POST /save?name=<file>.json  -> writes google-play/<file>.json (name must match [a-z0-9-]+\\.json). Stop with Ctrl+C or kill."""
import http.server, pathlib, re, urllib.parse
OUT = pathlib.Path(__file__).parent / "google-play"
class H(http.server.BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "https://play.google.com")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "content-type")
        self.send_header("Access-Control-Allow-Private-Network", "true")
    def do_OPTIONS(self):
        self.send_response(204); self._cors(); self.end_headers()
    def do_POST(self):
        q = urllib.parse.urlparse(self.path); name = urllib.parse.parse_qs(q.query).get("name", [""])[0]
        if q.path != "/save" or not re.fullmatch(r"[a-z0-9-]+\.json", name):
            self.send_response(400); self._cors(); self.end_headers(); return
        body = self.rfile.read(int(self.headers.get("content-length", 0)))
        (OUT / name).write_bytes(body)
        self.send_response(200); self._cors(); self.end_headers(); self.wfile.write(str(len(body)).encode())
    def log_message(self, *a): pass
http.server.HTTPServer(("127.0.0.1", 8765), H).serve_forever()
