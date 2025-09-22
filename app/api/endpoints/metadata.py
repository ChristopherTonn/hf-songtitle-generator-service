from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.song_title_data import song_title_data

router = APIRouter()

class MetadataResponse(BaseModel):
    genres: List[str]
    moods: List[str]

@router.get("", response_model=MetadataResponse)
def get_metadata():
    """Get available genres and moods for the frontend UI elements."""
    # Extract genres (excluding extended_mood_map)
    genres = [key for key in song_title_data.keys() if key != "extended_mood_map"]
    
    # Extract moods from extended_mood_map
    moods = list(song_title_data["extended_mood_map"].keys())
    
    return {
        "genres": sorted(genres),
        "moods": sorted(moods)
    }