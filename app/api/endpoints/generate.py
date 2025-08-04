from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
from app.core.title_generator import generate_song_title

router = APIRouter()

class GenerateTitleRequest(BaseModel):
    genre: str
    mood: str
    custom_words: Optional[List[str]] = None

class GenerateTitleResponse(BaseModel):
    title: str

@router.post("/generate-title", response_model=GenerateTitleResponse)
def generate_title(request: GenerateTitleRequest):
    title = generate_song_title(
        genre=request.genre.lower(),
        mood=request.mood,
        custom_words=request.custom_words
    )
    return {"title": title}