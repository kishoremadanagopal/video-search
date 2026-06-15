from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class VideoResponse(BaseModel):
    """Shape of a Video as returned by the API."""
    id: int
    title: str
    source_url: Optional[str] = None
    storage_key: Optional[str] = None
    duration_seconds: Optional[float] = None
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # lets Pydantic read from SQLAlchemy ORM objects
