from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.database import create_db_and_tables
from app.routers import auth, movies, tv, watchlist, search
from app.api.routes import playback

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(title="Netflix Clone API", version="1.0.1", lifespan=lifespan)

# Configure CORS
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(movies.router)
app.include_router(tv.router)
app.include_router(watchlist.router)
app.include_router(search.router)
app.include_router(playback.router, prefix="/playback", tags=["playback"])
app.include_router(playback.router)

@app.get("/")
def read_root():
    return {"message": "Netflix Clone API is running"}
