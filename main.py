from fastapi import FastAPI
from typing import Literal
import uvicorn
from fastapi.responses import HTMLResponse
import readingDrSeus

app = FastAPI()

@app.get("/")
async def read_root():
    return readingDrSeus.my_poem

