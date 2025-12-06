from fastapi import FastAPI
from sqlmodel import SQLModel

from app.database import engine
from app.routes import heroes, ai
from app.routes.ai import ai_test_function


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()
app.include_router(ai.router)


#@app.on_event("startup")
#def on_startup():
#    create_db_and_tables()
#
#
#app.include_router(heroes.router)


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/ai")
def ai_response():
    result =  ai_test_function()
    return {"response": result}