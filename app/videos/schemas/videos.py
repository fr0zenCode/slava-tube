import datetime

from pydantic import BaseModel


class CreateVideoSchema(BaseModel):
    video_path: str
    start_time: datetime.datetime
    duration: datetime.timedelta
    camera_number: int
    location: str


class CreateVideoResponseSchema(CreateVideoSchema):
    id: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True


class UpdateVideoStatusSchema(BaseModel):
    status: str
