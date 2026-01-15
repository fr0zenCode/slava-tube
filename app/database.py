from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DATABASE_URL = 'postgresql+psycopg2://postgres:postgres@db:5432/postgres'


engine = create_engine(DATABASE_URL)
session = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    ...


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
