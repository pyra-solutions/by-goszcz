from .clienteli.client import Client as ELIClient
from .clientsejm.client import Client as SejmClient
from .clientsejm.api.processes import get_sejm_termterm_processes
from fastapi import Depends, FastAPI, HTTPException
import httpx
from sqlmodel import SQLModel, Session, select
from pydantic import BaseModel

from app.database import engine, get_db
from app.models.models import ActInfo
from app.routes import  ai
from app.routes.ai import ai_clarify_act


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


create_db_and_tables()
app = FastAPI()

# app.include_router(ai.router)

eli_client = ELIClient(base_url="https://api.sejm.gov.pl/eli", timeout=httpx.Timeout(10.0))
sejm_client = SejmClient(base_url="https://api.sejm.gov.pl/", timeout=httpx.Timeout(10.0))


#ID aktu
class AiRequest(BaseModel):
    pos: int

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/acts/{page}", response_model=list[ActInfo])
def acts(
    page: int,
    page_size: int = 20,
    session: Session = Depends(get_db)
) -> list[ActInfo]:

    if page < 1:
        raise HTTPException(status_code=400, detail="Page must be >= 1")

    offset = (page - 1) * page_size

    query = select(ActInfo).offset(offset).limit(page_size)
    result = session.exec(query)
    acts = list(result.all())

    if not acts:
        raise HTTPException(status_code=404, detail="No acts on this page")

    return acts

@app.get("/act/{address}")
def act(address: str, session: Session = Depends(get_db)) -> ActInfo:
    # Get act from database using ORM
    act = session.get(ActInfo, {"address": address})
    
    if not act:
        raise HTTPException(status_code=404, detail="Act not found")

    return act


# nie ma response type bo to musi być w SQLModel
@app.get("/processes/{term}")
async def process(term: int):
    res = await get_sejm_termterm_processes.asyncio(client=sejm_client,term=term,offset=0,limit=3,sort_by="documentDate")
    print(res)
    if not res:
        raise HTTPException(status_code=404, detail="Process not found")

    # tutaj to_dict zwraca to jak originalny response, powinno być to najpierw zapisane do bazy danych i z niej zwracane wtedy też typ możemy podać
    return res[0].to_dict()



@app.post("/ai")
def ai_response(request: AiRequest, session: Session = Depends(get_db)):
    result =  ai_clarify_act(request.pos,session)
    return {"response": result}

