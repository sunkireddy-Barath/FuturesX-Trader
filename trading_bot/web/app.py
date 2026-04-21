import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

# Get the absolute path to the current file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Templates directory is relative to app.py
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

LOG_FILE = os.path.join(os.path.dirname(BASE_DIR), "trading_bot.log")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serves the dashboard home page.
    """
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = f.readlines()
            # Reverse to show newest logs first
            logs.reverse()
    
    return templates.TemplateResponse("index.html", {"request": request, "logs": logs})

@app.get("/api/logs")
async def get_logs():
    """
    Returns logs as JSON for AJAX updates.
    """
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = f.readlines()
            logs.reverse()
            return {"logs": logs}
    return {"logs": []}

def run(port=8000):
    uvicorn.run(app, host="0.0.0.0", port=port)

if __name__ == "__main__":
    run()
