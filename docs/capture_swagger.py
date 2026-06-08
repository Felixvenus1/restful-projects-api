"""Capture a screenshot of the live Swagger UI (ARTEFACT 02-D).

Starts the FastAPI app with uvicorn on an ephemeral port, opens /docs in a
headless Chromium via Playwright, expands the operations, and saves
docs/swagger_screenshot.png.

Prerequisites:
    pip install playwright
    playwright install chromium

Run from the project root:
    python docs/capture_swagger.py
"""

from __future__ import annotations

import socket
import sys
import threading
import time
from pathlib import Path

import uvicorn

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.app.main import app  # noqa: E402


def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def main() -> None:
    from playwright.sync_api import sync_playwright

    port = _free_port()
    config = uvicorn.Config(app, host="127.0.0.1", port=port, log_level="warning")
    server = uvicorn.Server(config)
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()

    # Wait for the server to accept connections.
    for _ in range(50):
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                break
        except OSError:
            time.sleep(0.1)

    out = Path(__file__).resolve().parent / "swagger_screenshot.png"
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1280, "height": 1024})
            page.goto(f"http://127.0.0.1:{port}/docs", wait_until="networkidle")
            # Expand all operation rows so the screenshot shows every endpoint.
            for btn in page.query_selector_all("button.opblock-summary-control"):
                try:
                    btn.click()
                except Exception:
                    pass
            page.wait_for_timeout(600)
            page.screenshot(path=str(out), full_page=True)
            browser.close()
        print(f"Wrote {out}")
    finally:
        server.should_exit = True
        thread.join(timeout=5)


if __name__ == "__main__":
    main()
