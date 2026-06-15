from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

from database import get_db
from models import Video
from schemas import VideoResponse
from storage import upload_video

router = APIRouter(prefix="/videos", tags=["videos"])


@router.post("", response_model=VideoResponse, status_code=201)
def create_video(
    title: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    """
    Upload a video file. Stores it in MinIO and creates a row in the videos table.
    The actual transcription happens asynchronously (added in the next card).
    """
    # Loose check that it's actually a video
    if not file.content_type or not file.content_type.startswith("video/"):
        raise HTTPException(status_code=400, detail="File must be a video")

    # Figure out the file size (MinIO needs this for put_object)
    file.file.seek(0, 2)  # jump to end
    file_size = file.file.tell()
    file.file.seek(0)  # back to start

    # Upload to MinIO
    storage_key = upload_video(
        file_data=file.file,
        file_size=file_size,
        content_type=file.content_type,
        original_filename=file.filename or "video.mp4",
    )

    # Create DB row
    video = Video(
        title=title,
        storage_key=storage_key,
        status="pending",
    )
    db.add(video)
    db.commit()
    db.refresh(video)

    return video
