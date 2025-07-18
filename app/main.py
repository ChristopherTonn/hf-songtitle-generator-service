from fastapi import FastAPI
from app.routes import generate
from app.song_title_data import song_title_data

app = FastAPI()

app.include_router(generate.router, prefix="/generate")

print("🎧 Available Genres:\n")

for key in song_title_data:
    if key != "extended_mood_map":
        print("-", key)
