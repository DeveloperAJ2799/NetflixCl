from fastapi import APIRouter
from app.services.omdb import get_movies_by_search, get_series_by_search

router = APIRouter(prefix="/search", tags=["search"])

@router.get("/multi")
async def search_multi(query: str, page: int = 1):
    # OMDb separates movie/series search. We'll search both and combine or just return movies for now.
    # To keep it simple and consistent with typical "multi" search expectations, let's fetch movies.
    return await get_movies_by_search(query, page)

@router.get("/movie")
async def search_movie(query: str, page: int = 1):
    return await get_movies_by_search(query, page)

@router.get("/tv")
async def search_tv(query: str, page: int = 1):
    return await get_series_by_search(query, page)
