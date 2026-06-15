from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import Base, engine
import models  # noqa: F401 - registers models with Base.metadata


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create any missing tables in Postgres
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown: nothing to clean up yet


app = FastAPI(title="video-search", lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}
