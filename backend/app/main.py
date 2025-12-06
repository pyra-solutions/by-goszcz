# from eli_for_polish_acts_client.client import Client as EliClient
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import SQLModel, Session

from app.database import engine, get_db
from app.models.models import ActInfo
# from app.routes import  ai
# from app.routes.ai import ai_test_function


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


create_db_and_tables()
app = FastAPI()

# app.include_router(ai.router)


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/act/{act_id}")
def acts(act_id: int, session: Session = Depends(get_db)):
    # Get act from database using ORM
    act = session.get(ActInfo, act_id)  # zmień Hero na Act
    
    if not act:
        raise HTTPException(status_code=404, detail="Act not found")

    return act


# @app.get("/ai")
# def ai_response():
#     result =  ai_test_function()
#     return {"response": result}
#
#
# def ai_clarification():
#     result =  ai_clarification()
#     return {"response": result}
