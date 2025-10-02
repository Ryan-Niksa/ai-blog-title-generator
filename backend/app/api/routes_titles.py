from fastapi import APIRouter, Query
from ..services.title_generator import generate_titles

router = APIRouter()

@router.get("/titles", response_model=list[str])
def suggest_titles(topic: str = Query(..., description="Topic to generate blog titles for"),
                   n: int = Query(5, ge=1, le=10, description="Number of suggestions")):
    return generate_titles(topic, n)
