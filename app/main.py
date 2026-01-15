import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.database import Base, engine
from app.videos.routes.videos_rest import videos_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(videos_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
