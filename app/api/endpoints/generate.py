from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.core.title_generator import generate_song_title

router = APIRouter()

class GenerateTitleRequest(BaseModel):
    genre: str
    mood: str = None
    custom_words: List[str] = None

class GenerateTitleResponse(BaseModel):
    title: str

@router.post("", response_model=GenerateTitleResponse)
def generate_title(request: GenerateTitleRequest):
    title = generate_song_title(
        genre=request.genre.lower(),
        mood=request.mood,
        custom_words=request.custom_words
    )
    return {"title": title}