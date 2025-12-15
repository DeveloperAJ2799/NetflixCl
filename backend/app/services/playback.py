from typing import Optional

def generate_embed_url(
    provider: str,
    imdb_id: str,
    type: str,
    season: Optional[int] = None,
    episode: Optional[int] = None
) -> str:
    # Normalize provider
    provider = provider.lower()
    
    if provider == "vidfast":
        # Format: https://vidfast.in/movie/{IMDB_ID}
        # Format: https://vidfast.in/tv/{IMDB_ID}/{SEASON}/{EPISODE}
        if type == "movie":
            return f"https://vidfast.in/movie/{imdb_id}"
        elif type == "tv":
            if not season or not episode:
                 # Fallback or error, but let's default to season 1 ep 1 if missing for TV? 
                 # Or just return base. Let's assume input is valid.
                 return f"https://vidfast.in/tv/{imdb_id}/1/1"
            return f"https://vidfast.in/tv/{imdb_id}/{season}/{episode}"
            
    else:
        # Default to vidsrc (using vidsrc.pro as verified working source)
        # Format: https://vidsrc.pro/embed/movie/{IMDB_ID}
        # Format: https://vidsrc.pro/embed/tv/{IMDB_ID}/{SEASON}/{EPISODE}
        base_domain = "https://vidsrc.pro" 
        
        if type == "movie":
            return f"{base_domain}/embed/movie/{imdb_id}"
        elif type == "tv":
            if not season or not episode:
                return f"{base_domain}/embed/tv/{imdb_id}/1/1"
            return f"{base_domain}/embed/tv/{imdb_id}/{season}/{episode}"
    
    return ""
