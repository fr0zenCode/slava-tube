import datetime
from typing import List

from starlette import status
from fastapi import APIRouter, Depends, Query
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.videos.schemas.videos import (
    CreateVideoResponseSchema,
    CreateVideoSchema,
    UpdateVideoStatusSchema
)
from app.database import get_db
from app.videos.models.videos import Video


videos_router = APIRouter(prefix='/videos', tags=['videos'])


@videos_router.post(
    '',
    response_model=CreateVideoResponseSchema
)
def create_video(data: CreateVideoSchema, db: Session = Depends(get_db)):
    try:
        video = Video(**data.model_dump(), status='new')
        db.add(video)
        db.commit()
        db.refresh(video)
        return video
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)


@videos_router.get(
    '',
    response_model=List[CreateVideoResponseSchema]
)
def get_videos(
    status: List[str] | None = Query(None),
    camera_number: List[int] | None = Query(None),
    location: List[str] | None = Query(None),
    start_time_from: datetime.datetime = None,
    start_time_to: datetime.datetime = None,
    db: Session = Depends(get_db),
):
    query = db.query(Video)

    if status:
        query = query.filter(Video.status.in_(status))
    if camera_number:
        query = query.filter(Video.camera_number.in_(camera_number))
    if location:
        query = query.filter(Video.location.in_(location))
    if start_time_from:
        query = query.filter(Video.start_time >= start_time_from)
    if start_time_to:
        query = query.filter(Video.start_time <= start_time_to)

    return query.all()


@videos_router.get('/{video_id}', response_model=CreateVideoResponseSchema)
def get_video_by_id(video_id: int, db: Session = Depends(get_db)):
    video = db.get(Video, video_id)
    if not video:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Video not found'
        )
    return video


@videos_router.patch(
        '/{video_id}/status',
        response_model=CreateVideoResponseSchema
    )
def update_video_status_by_video_id(
    video_id: int,
    data: UpdateVideoStatusSchema,
    db: Session = Depends(get_db),
):
    video = get_video_by_id(video_id=video_id, db=db)
    video.status = data.status
    try:
        db.commit()
        db.refresh(video)
        return video
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
