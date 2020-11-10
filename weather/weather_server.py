from weather import whereami, current_weather
from dataclasses import asdict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    here = await whereami()
    weather = await current_weather(here.latitude, here.longitude)
    return {**asdict(here), **asdict(weather)}
