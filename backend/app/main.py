from fastapi import FastAPI
from sqlmodel import SQLModel

from app.database import engine
from app.routes import heroes


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(heroes.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
