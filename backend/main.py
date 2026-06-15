from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import Base, engine
from storage import ensure_bucket
from routers.videos import router as videos_router
import models  # noqa: F401 - registers models with Base.metadata


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create any missing tables + make sure MinIO bucket exists
    Base.metadata.create_all(bind=engine)
    ensure_bucket()
    yield
    # Shutdown: nothing to clean up yet


app = FastAPI(title="video-search", lifespan=lifespan)

app.include_router(videos_router)


@app.get("/health")
def health():
    return {"status": "ok"}
