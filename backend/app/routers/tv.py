from fastapi import APIRouter
from app.services import omdb

router = APIRouter(prefix="/tv", tags=["tv"])

@router.get("/popular")
async def get_popular_tv():
    # Simulated "popular" by searching for a broad term
    data = await omdb.get_series_by_search("Review")
    return data

@router.get("/{imdb_id}")
async def get_tv_details(imdb_id: str):
    return await omdb.get_details(imdb_id)

@router.get("/{imdb_id}/season/{season}")
async def get_tv_season(imdb_id: str, season: int):
    return await omdb.get_season_episodes(imdb_id, season)
