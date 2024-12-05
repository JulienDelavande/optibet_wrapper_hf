from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

FRONTEND_URL = "https://optibet.delavande.fr/"

@app.get("/{path:path}")
async def redirect_to_frontend(path: str):
    return RedirectResponse(f"{FRONTEND_URL}/{path}")

@app.get("/")
async def home():
    return RedirectResponse(FRONTEND_URL)
