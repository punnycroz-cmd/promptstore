from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse


BASE_DIR = Path(__file__).resolve().parent
HTML_FILE = BASE_DIR / "public" / "frontend.html"

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index():
    return HTML_FILE.read_text(encoding="utf-8")


@app.get("/health")
def health():
    return {"ok": True}
