from pydantic import BaseModel
from typing import Optional

class PlaybackRequest(BaseModel):
    imdb_id: str
    provider: str = "vidsrc"  # "vidsrc" or "vidfast"
    type: str = "movie"      # "movie" or "tv"
    season: Optional[int] = None
    episode: Optional[int] = None

class PlaybackResponse(BaseModel):
    embed_url: str
    provider: str
