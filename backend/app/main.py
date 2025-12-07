from .clienteli.client import Client as ELIClient
from .clientsejm.client import Client as SejmClient
from .clientsejm.api.processes import get_sejm_termterm_processes
from fastapi import Depends, FastAPI, HTTPException
import httpx
from sqlmodel import SQLModel, Session, select
from pydantic import BaseModel

from app.database import engine, get_db
from app.models.models import ActInfo, Comment, Consultation
from app.models.models import ProcessHeader
from app.routes import  ai
from app.routes.ai import ai_clarify_act
from fastapi.middleware.cors import CORSMiddleware


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


create_db_and_tables()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # <--- allow all origins
    allow_credentials=True,
    allow_methods=["*"],           # <--- allow all HTTP methods
    allow_headers=["*"],           # <--- allow all headers
)

# app.include_router(ai.router)

eli_client = ELIClient(base_url="https://api.sejm.gov.pl/eli", timeout=httpx.Timeout(10.0))
sejm_client = SejmClient(base_url="https://api.sejm.gov.pl/", timeout=httpx.Timeout(10.0))


##ID aktu
#class AiRequest(BaseModel):
#    pos: int


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


# use - instead of / in id
@app.get("/comments-by-consultation-id/{consultation_id}", response_model=list[Comment])
def comments_by_consultation_id(
    consultation_id: str,
    session: Session = Depends(get_db)
) -> list[Comment]:

    query = select(Comment).where(Comment.consultation_id==consultation_id.replace("-","/"))
    result = session.exec(query)
    comments = list(result.all())

    if not comments:
        raise HTTPException(status_code=404, detail="No comments for this project id")

    return comments

@app.get("/consultations-by-project-id/{project_id}", response_model=list[Consultation])
def consultations_by_project_id(
    project_id: int,
    session: Session = Depends(get_db)
) -> list[Consultation]:

    query = select(Consultation).where(Consultation.project_pos == project_id)
    result = session.exec(query)
    consultations = list(result.all())

    if not consultations:
        raise HTTPException(status_code=404, detail="No consultations for this project id")

    return consultations

@app.get("/consultations/{page}", response_model=list[Consultation])
def consultations(
    page: int,
    page_size: int = 20,
    session: Session = Depends(get_db)
) -> list[Consultation]:

    if page < 1:
        raise HTTPException(status_code=400, detail="Page must be >= 1")

    offset = (page - 1) * page_size

    query = select(Consultation).offset(offset).limit(page_size)
    result = session.exec(query)
    consultations = list(result.all())

    if not consultations:
        raise HTTPException(status_code=404, detail="No consultations on this page")

    return consultations

## nie ma response type bo to musi być w SQLModel
#@app.get("/processes/{term}")
#@app.get("/term{term}/processes", response_model=list[ProcessHeader])
#def processes(
#    term: int,
#    page: int = 1,
#    page_size: int = 20,
#    session: Session = Depends(get_db)
#) -> list[ProcessHeader]:
#    """
#    Get processes from database for a given term with pagination.
#    """
#    if page < 1:
#        raise HTTPException(status_code=400, detail="Page must be >= 1")
#
#    offset = (page - 1) * page_size
#
#    query = select(ProcessHeader).where(ProcessHeader.term == term).offset(offset).limit(page_size)
#    result = session.exec(query)
#    processes = list(result.all())
#
#    if not processes:
#        raise HTTPException(status_code=404, detail="No processes found for this term")
#
#    return processes
async def fetch_and_save_processes(term: int, session: Session):
    """
    Fetches processes from API and saves them to database if not already present.
    """
    offset = 0
    limit = 100
    saved_count = 0
    
    while True:
        processes_response = await get_sejm_termterm_processes.asyncio(
            client=sejm_client,
            term=term,
            offset=offset,
            limit=limit
        )
        
        if not processes_response:
            break
        
        for process_api in processes_response:
            process_dict = process_api.to_dict()
            
            # Check if process already exists in database
            existing = session.exec(
                select(ProcessHeader).where(
                    ProcessHeader.term == term,
                    ProcessHeader.number == process_dict.get("number")
                )
            ).first()
            
            if existing:
                continue
            
            process_db = ProcessHeader(
                term=process_dict.get("term"),
                number=process_dict.get("number"),
                title=process_dict.get("title"),
                title_final=process_dict.get("titleFinal"),
                description=process_dict.get("description"),
                document_date=process_dict.get("documentDate"),
                process_start_date=process_dict.get("processStartDate"),
                change_date=process_dict.get("changeDate"),
                document_type=process_dict.get("documentType"),
                document_type_enum=process_dict.get("documentTypeEnum"),
                comments=process_dict.get("comments"),
                web_generated_date=process_dict.get("webGeneratedDate"),
                closure_date=process_dict.get("closureDate"),
                address=process_dict.get("address"),
                display_address=process_dict.get("displayAddress"),
                eli=process_dict.get("ELI"),
                passed=process_dict.get("passed"),
                shorten_procedure=process_dict.get("shortenProcedure"),
                urgency_status=process_dict.get("urgencyStatus"),
                urgency_withdraw_date=process_dict.get("urgencyWithdrawDate")
            )
            
            session.add(process_db)
            saved_count += 1
        
        if len(processes_response) < limit:
            break
        
        offset += limit
    
    if saved_count > 0:
        session.commit()
    
    return saved_count


@app.get("/term{term}/processes", response_model=list[ProcessHeader])
async def processes(
    term: int,
    page: int = 1,
    page_size: int = 20,
    session: Session = Depends(get_db)
) -> list[ProcessHeader]:
    """
    Get processes from database for a given term with pagination.
    Fetches from API if not in database.
    """
    if page < 1:
        raise HTTPException(status_code=400, detail="Page must be >= 1")

    # Check if we have any processes for this term in database
    count_query = select(ProcessHeader).where(ProcessHeader.term == term)
    existing_count = len(list(session.exec(count_query).all()))
    
    # If no processes found, fetch from API
    if existing_count == 0:
        print(f"No processes found in database for term {term}, fetching from API...")
        saved = await fetch_and_save_processes(term, session)
        print(f"Saved {saved} processes to database")

    offset = (page - 1) * page_size

    query = select(ProcessHeader).where(ProcessHeader.term == term).offset(offset).limit(page_size)
    result = session.exec(query)
    processes = list(result.all())

    if not processes:
        raise HTTPException(status_code=404, detail="No processes found for this term")

    return processes
#


#@app.post("/ai")
#async def ai_response(request: AiRequest, session: Session = Depends(get_db)):
#    result =  await ai_clarify_act(request.pos,session)
#    return {"response": result}

@app.get("/ai")
async def ai_response(pos: int, session: Session = Depends(get_db)):
    result = await ai_clarify_act(pos, session)
    return {"response": result}
