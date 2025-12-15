from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List

from app.database import get_session
from app.models import User, Watchlist, WatchlistCreate, WatchlistRead
from app.auth import get_current_user

router = APIRouter(prefix="/watchlist", tags=["watchlist"])

@router.get("/", response_model=List[WatchlistRead])
def get_watchlist(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    statement = select(Watchlist).where(Watchlist.user_id == current_user.id)
    results = session.exec(statement).all()
    return results

@router.post("/", response_model=WatchlistRead)
def add_to_watchlist(
    item: WatchlistCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    # Check if already exists
    statement = select(Watchlist).where(
        Watchlist.user_id == current_user.id,
        Watchlist.imdb_id == item.imdb_id
    )
    existing = session.exec(statement).first()
    if existing:
        return existing

    watchlist_item = Watchlist.from_orm(item)
    watchlist_item.user_id = current_user.id
    session.add(watchlist_item)
    session.commit()
    session.refresh(watchlist_item)
    return watchlist_item

@router.delete("/{imdb_id}")
def remove_from_watchlist(
    imdb_id: str,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    statement = select(Watchlist).where(
        Watchlist.user_id == current_user.id,
        Watchlist.imdb_id == imdb_id
    )
    results = session.exec(statement)
    item = results.first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found in watchlist")
    
    session.delete(item)
    session.commit()
    return {"ok": True}
