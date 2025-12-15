from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime

class UserBase(SQLModel):
    email: str = Field(index=True, unique=True)
    full_name: Optional[str] = None
    is_active: bool = True
    is_superuser: bool = False

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    created_at: datetime

class Token(SQLModel):
    access_token: str
    token_type: str

class TokenData(SQLModel):
    email: Optional[str] = None

class WatchlistBase(SQLModel):
    imdb_id: str = Field(index=True)
    title: str
    poster_url: Optional[str] = None
    media_type: str = "movie" # movie or tv

class Watchlist(WatchlistBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    added_at: datetime = Field(default_factory=datetime.utcnow)

class WatchlistCreate(WatchlistBase):
    pass

class WatchlistRead(WatchlistBase):
    id: int
    user_id: int
