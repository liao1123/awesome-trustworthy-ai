#!/usr/bin/env python3
"""Local reader server with star-event collector.

Serves reader/ (index.html, app.js, style.css, data/papers.js) and accepts
POST /api/stars to persist star events to tools/out/starred-live.json so the
assistant can read preferences in real time. Binds 127.0.0.1 only — access it
through an SSH/VSCode port forward, e.g. VSCode Ports panel -> forward 8765.

Usage: python3 tools/serve_reader.py [port]
"""

from __future__ import annotations

import json
import sys
import tempfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
READER = ROOT / "reader"
STARS = Path(__file__).resolve().parent / "starred-live.json"
LOCAL_DATA = Path(__file__).resolve().parent / "data"  # reader/build.py --local output (includes idea/)

CONTENT_TYPES = {
    ".html": "text/html; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".json": "application/json; charset=utf-8",
}


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):  # quiet
        pass

    def _send(self, code: int, body: bytes, ctype: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        path = self.path.split("?")[0]
        if path in ("/api/ping",):
            self._send(200, b'{"ok":true}', "application/json")
            return
        if path == "/":
            path = "/index.html"
        # prefer the local-only dataset (idea/ included) when present
        if path == "/data/papers.js":
            local = LOCAL_DATA / "papers.js"
            if local.is_file():
                self._send(200, local.read_bytes(), "application/javascript; charset=utf-8")
                return
        target = (READER / path.lstrip("/")).resolve()
        if not str(target).startswith(str(READER)) or not target.is_file():
            self._send(404, b"not found", "text/plain; charset=utf-8")
            return
        ctype = CONTENT_TYPES.get(target.suffix, "application/octet-stream")
        self._send(200, target.read_bytes(), ctype)

    def do_POST(self) -> None:  # noqa: N802
        if self.path.split("?")[0] != "/api/stars":
            self._send(404, b"not found", "text/plain; charset=utf-8")
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length) or b"{}")
            if not isinstance(payload, dict):
                raise ValueError("expected object")
            payload["received"] = __import__("datetime").datetime.now().isoformat(timespec="seconds")
            STARS.parent.mkdir(parents=True, exist_ok=True)
            # atomic-ish write: temp file then replace
            with tempfile.NamedTemporaryFile("w", dir=STARS.parent, delete=False,
                                             encoding="utf-8", suffix=".tmp") as fh:
                json.dump(payload, fh, ensure_ascii=False, indent=1)
                tmp = fh.name
            Path(tmp).replace(STARS)
            self._send(200, b'{"ok":true}', "application/json")
        except Exception as e:  # noqa: BLE001
            self._send(400, json.dumps({"ok": False, "error": str(e)}).encode(), "application/json")


def main() -> int:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"reader + star collector on http://127.0.0.1:{port} "
          f"(stars -> {STARS})", flush=True)
    server.serve_forever()
    return 0


if __name__ == "__main__":
    sys.exit(main())
