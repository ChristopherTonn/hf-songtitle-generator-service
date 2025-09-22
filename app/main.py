from fastapi import FastAPI
from app.api.endpoints.generate import router as generate_router
from app.api.endpoints.metadata import router as metadata_router


app = FastAPI(
    title="Song Title Generator API",
    description="Generate creative song titles based on genre, mood and style.",
    version="1.0.0")

app.include_router(generate_router, prefix="/generate", tags=["Generate"])
app.include_router(metadata_router, prefix="/metadata", tags=["Metadata"])