from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.song_title_data import song_title_data

router = APIRouter()

class MetadataResponse(BaseModel):
    genres: List[str]
    moods: List[str]

@router.get("/", response_model=MetadataResponse)
def get_metadata():
    """Get available genres and moods for frontend UI elements."""
    # Available genres from song_title_data (exclude extended_mood_map)
    available_genres = sorted([
        genre for genre in song_title_data.keys() 
        if genre != "extended_mood_map"
    ])
    
    # Available moods from extended_mood_map
    available_moods = sorted(list(song_title_data.get("extended_mood_map", {}).keys()))
    
    return {
        "genres": available_genres,
        "moods": available_moods
    }