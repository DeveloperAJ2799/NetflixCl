from fastapi import APIRouter, HTTPException, Query
from app.schemas.playback import PlaybackResponse
from app.services.playback import generate_embed_url

router = APIRouter()

@router.get("/url", response_model=PlaybackResponse)
def get_playback_url(
    imdb_id: str,
    provider: str = "vidsrc",
    type: str = "movie",
    season: int = Query(None),
    episode: int = Query(None)
):
    """
    Generate an embed URL for the specified provider and content.
    """
    url = generate_embed_url(
        provider=provider,
        imdb_id=imdb_id,
        type=type,
        season=season,
        episode=episode
    )
    
    if not url:
        raise HTTPException(status_code=400, detail="Could not generate playback URL")

    return PlaybackResponse(embed_url=url, provider=provider)
