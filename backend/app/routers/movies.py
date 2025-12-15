from fastapi import APIRouter
from typing import List
from app.services.omdb import get_movies_by_search, get_details

router = APIRouter(prefix="/movies", tags=["movies"])

@router.get("/trending")
async def get_trending():
    # Simulate trending with a popular search term
    return await get_movies_by_search("Marvel")

@router.get("/popular")
async def get_popular():
    return await get_movies_by_search("Star Wars")

@router.get("/action")
async def get_action():
    return await get_movies_by_search("Action")

@router.get("/comedy")
async def get_comedy():
    return await get_movies_by_search("Comedy")

@router.get("/{imdb_id}")
async def get_movie_details(imdb_id: str):
    return await get_details(imdb_id)
