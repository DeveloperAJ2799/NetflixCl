import httpx
from fastapi import HTTPException
from pydantic_settings import BaseSettings
from datetime import datetime, timedelta

class Settings(BaseSettings):
    omdb_api_key: str

    class Config:
        env_file = ".env"

settings = Settings()
OMDB_URL = "http://www.omdbapi.com/"

# Simple in-memory cache: { "url_param_string": { "data": response_json, "expires": datetime } }
CACHE = {}
CACHE_DURATION_MINUTES = 60

async def fetch_omdb_data(params: dict):
    # Construct cache key from sorted params
    params["apikey"] = settings.omdb_api_key
    cache_key = tuple(sorted(params.items()))
    
    # Check cache
    if cache_key in CACHE:
        cached_item = CACHE[cache_key]
        if datetime.utcnow() < cached_item["expires"]:
             return cached_item["data"]
        else:
             del CACHE[cache_key] # Expired

    async with httpx.AsyncClient() as client:
        response = await client.get(OMDB_URL, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="OMDb API Error")
        data = response.json()
        
        # OMDb returns 200 even for errors
        if data.get("Response") == "False":
             # Don't cache errors? Or cache them briefly? Let's return without caching for now
             return data
        
        # Save to cache
        CACHE[cache_key] = {
            "data": data,
            "expires": datetime.utcnow() + timedelta(minutes=CACHE_DURATION_MINUTES)
        }
        
        return data

def filter_unreleased(items: list) -> list:
    current_year = datetime.now().year
    filtered = []
    for item in items:
        year_str = item.get("Year", "")
        # Handle "2022–" or "2025"
        clean_year = year_str.split("–")[0].strip()
        if clean_year.isdigit() and int(clean_year) > current_year:
            continue
        filtered.append(item)
    return filtered

async def get_movies_by_search(query: str, page: int = 1):
    data = await fetch_omdb_data({"s": query, "page": page, "type": "movie"})
    if data.get("Response") == "True":
        return filter_unreleased(data.get("Search", []))
    return []

async def get_series_by_search(query: str, page: int = 1):
    data = await fetch_omdb_data({"s": query, "page": page, "type": "series"})
    if data.get("Response") == "True":
        return filter_unreleased(data.get("Search", []))
    return []

async def get_details(imdb_id: str):
    data = await fetch_omdb_data({"i": imdb_id, "plot": "full"})
    return data

async def get_season_episodes(imdb_id: str, season: int):
    data = await fetch_omdb_data({"i": imdb_id, "Season": season})
    if data.get("Response") == "True":
        return data.get("Episodes", [])
    return []
