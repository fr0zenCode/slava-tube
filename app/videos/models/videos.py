from datetime import datetime, timedelta

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Interval,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.database import Base


class Video(Base):
    __tablename__ = 'videos'

    __table_args__ = (
        CheckConstraint("duration > interval '0 seconds'", name='duration_positive'),
        CheckConstraint('camera_number > 0', name='camera_number_positive'),
        CheckConstraint('length(video_path) > 0', name='video_path_not_blank'),
        CheckConstraint('length(location) > 0', name='location_not_blank'),
        CheckConstraint("status IN ('new', 'transcoded', 'recognized')", name='status_in_list')
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    video_path: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment='Путь к видео',
    )

    start_time: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        comment='Время начала видео',
    )

    duration: Mapped[timedelta] = mapped_column(
        Interval,
        nullable=False,
        comment='Продолжительность видео',
    )

    camera_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        comment='Номер камеры',
    )

    location: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment='Локация камеры',
    )

    status: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default='new',
        server_default='new',
        comment='new | transcoded | recognized',
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        comment='Время создания ролика',
    )
