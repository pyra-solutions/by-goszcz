from .clienteli.client import Client as ELIClient
from .clientsejm.client import Client as SejmClient
from .clientsejm.api.processes import get_sejm_termterm_processes, get_sejm_termterm_processes_num
from fastapi import Depends, FastAPI, HTTPException
import httpx
import re
from bs4 import BeautifulSoup
from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Session, select
from pydantic import BaseModel

from app.database import engine, get_db
from app.models.models import ActInfo, Comment, Consultation, ProcessDetails, LegislationAct
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

BASE_URL = "https://legislacja.rcl.gov.pl"


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
        print(f"Fetching processes from Sejm API for term {term}, offset {offset}, limit {limit}...")
        try:
            processes_response = await get_sejm_termterm_processes.asyncio(
                client=sejm_client,
                term=term,
                offset=offset,
                limit=limit
            )
            print(f"Raw processes_response from API: {processes_response}") # Debug print
        except Exception as e:
            print(f"Error calling Sejm API: {e}")
            processes_response = None
        
        if not processes_response: # <--- This is where it could break if processes_response is empty
            print(f"No more processes or empty response from Sejm API for term {term}.")
            break
        
        print(f"Received {len(processes_response)} processes from Sejm API.")
        
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
        return []

    return processes

class CombinedItem(BaseModel):
    id: str
    type: str
    title: str
    date: Optional[datetime]
    status: Optional[str] = None
    description: Optional[str] = None
    source_id: str
    url: Optional[str] = None
    stages: Optional[List[dict]] = []
    links: Optional[List[dict]] = []
    term: Optional[int] = None
    sejm_id: Optional[str] = None

@app.get("/combined", response_model=list[CombinedItem])
def combined_feed(
    page: int = 1,
    page_size: int = 20,
    q: Optional[str] = None,
    session: Session = Depends(get_db)
) -> list[CombinedItem]:
    if page < 1:
        raise HTTPException(status_code=400, detail="Page must be >= 1")
    
    limit = page_size
    
    # Legislation
    leg_query = select(LegislationAct).order_by(LegislationAct.date_created.desc())
    if q:
        leg_query = leg_query.where(LegislationAct.title.ilike(f"%{q}%"))
    leg_items = session.exec(leg_query.limit(limit * page)).all()
    
    # Consultations
    cons_query = select(Consultation).order_by(Consultation.start_date.desc())
    if q:
        cons_query = cons_query.where(Consultation.project_name.ilike(f"%{q}%"))
    cons_items = session.exec(cons_query.limit(limit * page)).all()

    # Processes
    proc_query = select(ProcessHeader).order_by(ProcessHeader.change_date.desc())
    if q:
        proc_query = proc_query.where(ProcessHeader.title.ilike(f"%{q}%"))
    proc_items = session.exec(proc_query.limit(limit * page)).all()

    combined = []
    
    for item in leg_items:
        combined.append(CombinedItem(
            id=f"leg-{item.id}",
            type="legislation",
            title=item.title,
            date=item.date_created,
            status=item.status,
            description=f"Applicant: {item.applicant}",
            source_id=str(item.id),
            url=item.link,
            stages=item.stages or [],
            links=[{"href": item.link, "rel": "self"}] if item.link else [],
            sejm_id=item.sejm_id
        ))
        
    for item in cons_items:
        combined.append(CombinedItem(
            id=f"cons-{item.id}",
            type="consultation",
            title=item.project_name,
            date=item.start_date,
            status=item.status,
            description=item.description,
            source_id=str(item.id),
            url=None,
            stages=[],
            links=[]
        ))

    for item in proc_items:
        combined.append(CombinedItem(
            id=f"proc-{item.id}",
            type="process",
            title=item.title or "No Title",
            date=item.change_date or item.process_start_date,
            status="Uchwalono" if item.passed else "W toku",
            description=item.description,
            source_id=str(item.id),
            url=None,
            stages=[], # Header doesn't have stages
            links=[]
        ))
        
    combined.sort(key=lambda x: x.date if x.date else datetime.min, reverse=True)
    
    start = (page - 1) * page_size
    end = start + page_size
    
    if start >= len(combined):
        return []
        
    return combined[start:end]

@app.get("/project/{project_number}", response_model=list[CombinedItem])
async def project_details_combined(
    project_number: str,
    term: Optional[int] = None,
    session: Session = Depends(get_db)
) -> list[CombinedItem]:
    """
    Get all combined items related to a specific project number from various sources.
    Includes stages and links.
    Optional 'term' parameter to filter Sejm processes by term (e.g., 9 or 10).
    """
    combined = []
    
    # 1. LegislationAct
    leg_items = session.exec(
        select(LegislationAct).where(LegislationAct.number == project_number)
    ).all()
    
    for item in leg_items:
        combined.append(CombinedItem(
            id=f"leg-{item.id}",
            type="legislation",
            title=item.title,
            date=item.date_created,
            status=item.status,
            description=f"Applicant: {item.applicant}",
            source_id=str(item.id),
            url=item.link,
            stages=[],
            links=[{"href": item.link, "rel": "self"}] if item.link else []
        ))

    # 2. ProcessHeader
    proc_query = select(ProcessHeader).where(ProcessHeader.number == project_number)
    if term:
        proc_query = proc_query.where(ProcessHeader.term == term)
    proc_items = session.exec(proc_query).all()
    
    for item in proc_items:
        # Try to find details to get stages
        stages = []
        links = []
        
        if item.term:
            details = session.exec(
                select(ProcessDetails).where(
                    ProcessDetails.term == item.term,
                    ProcessDetails.number == item.number
                )
            ).first()
            if details:
                stages = details.stages or []
                links = details.links or []
            else:
                # Try API
                try:
                    # print(f"Fetching details from API for term {item.term}, number {item.number}")
                    process_response = await get_sejm_termterm_processes_num.asyncio(
                        client=sejm_client,
                        term=item.term,
                        num=item.number
                    )
                    if process_response:
                        process_dict = process_response.to_dict()
                        # Create DB object
                        process_details_db = ProcessDetails(
                            term=process_dict.get("term"),
                            number=process_dict.get("number"),
                            title=process_dict.get("title"),
                            description=process_dict.get("description"),
                            u_e=process_dict.get("UE"),
                            document_date=process_dict.get("documentDate"),
                            change_date=process_dict.get("changeDate"),
                            web_generated_date=process_dict.get("webGeneratedDate"),
                            process_start_date=process_dict.get("processStartDate"),
                            document_type=process_dict.get("documentType"),
                            document_type_enum=process_dict.get("documentTypeEnum"),
                            comments=process_dict.get("comments"),
                            prints_considered_jointly=process_dict.get("printsConsideredJointly", []),
                            title_final=process_dict.get("titleFinal"),
                            closure_date=process_dict.get("closureDate"),
                            address=process_dict.get("address"),
                            display_address=process_dict.get("displayAddress"),
                            e_li=process_dict.get("ELI"),
                            passed=process_dict.get("passed"),
                            shorten_procedure=process_dict.get("shortenProcedure"),
                            urgency_status=process_dict.get("urgencyStatus"),
                            urgency_withdraw_date=process_dict.get("urgencyWithdrawDate"),
                            other_documents=process_dict.get("otherDocuments", []),
                            rcl_num=process_dict.get("rclNum"),
                            rcl_link=process_dict.get("rclLink"),
                            legislative_committee=process_dict.get("legislativeCommittee"),
                            principle_of_subsidiarity=process_dict.get("principleOfSubsidiarity"),
                            stages=process_dict.get("stages", []),
                            links=process_dict.get("links", [])    
                        )
                        session.add(process_details_db)
                        session.commit()
                        stages = process_dict.get("stages", [])
                        links = process_dict.get("links", [])
                except Exception as e:
                    print(f"Error fetching details for {item.number}: {e}")
        
        combined.append(CombinedItem(
            id=f"proc-{item.id}",
            type="process",
            title=item.title or "No Title",
            date=item.change_date or item.process_start_date,
            status="Uchwalono" if item.passed else "W toku",
            description=item.description,
            source_id=str(item.id),
            url=None,
            stages=stages,
            links=links,
            term=item.term
        ))

    # 3. ProcessDetails (match on rcl_num)
    det_query = select(ProcessDetails).where(ProcessDetails.rcl_num == project_number)
    if term:
        det_query = det_query.where(ProcessDetails.term == term)
    proc_details = session.exec(det_query).all()
    
    for item in proc_details:
        combined.append(CombinedItem(
            id=f"proc-det-{item.id}",
            type="process_detail",
            title=item.title or "No Title",
            date=item.change_date or item.process_start_date,
            status="Uchwalono" if item.passed else "W toku",
            description=item.description,
            source_id=str(item.id),
            url=None,
            stages=item.stages or [],
            links=item.links or [],
            term=item.term
        ))

    # 4. Consultation
    cons_items = session.exec(
        select(Consultation).where(Consultation.project_name.ilike(f"%{project_number}%"))
    ).all()
    
    for item in cons_items:
        combined.append(CombinedItem(
            id=f"cons-{item.id}",
            type="consultation",
            title=item.project_name,
            date=item.start_date,
            status=item.status,
            description=item.description,
            source_id=str(item.id),
            url=None,
            stages=[],
            links=[]
        ))

    combined.sort(key=lambda x: x.date if x.date else datetime.min, reverse=True)
    
    return combined

@app.get("/term{term}/processes/{num}")
async def process_details(
    term: int,
    num: str,
    session: Session = Depends(get_db)
) -> dict:
    """
    Get detailed process information for a specific term and process number.
    Fetches from API if not in database.
    """
    # Check if process details exist in database
    query = select(ProcessDetails).where(
        ProcessDetails.term == term,
        ProcessDetails.number == num
    )
    existing = session.exec(query).first()
    
    if existing:
        # Convert to dict to return full data
        return existing.model_dump()
    
    # If not found, fetch from API
    print(f"Process details not found in database for term {term}, number {num}, fetching from API...")
    
    try:
        process_response = await get_sejm_termterm_processes_num.asyncio(
            client=sejm_client,
            term=term,
            num=num
        )
        
        if not process_response:
            raise HTTPException(status_code=404, detail=f"Process {num} not found for term {term}")
        
        process_dict = process_response.to_dict()
        
        # Return the full API response as-is
        # Store simplified version in database for future reference
        process_details_db = ProcessDetails(
            term=process_dict.get("term"),
            number=process_dict.get("number"),
            title=process_dict.get("title"),
            description=process_dict.get("description"),
            u_e=process_dict.get("UE"),
            document_date=process_dict.get("documentDate"),
            change_date=process_dict.get("changeDate"),
            web_generated_date=process_dict.get("webGeneratedDate"),
            process_start_date=process_dict.get("processStartDate"),
            document_type=process_dict.get("documentType"),
            document_type_enum=process_dict.get("documentTypeEnum"),
            comments=process_dict.get("comments"),
            prints_considered_jointly=process_dict.get("printsConsideredJointly", []),
            title_final=process_dict.get("titleFinal"),
            closure_date=process_dict.get("closureDate"),
            address=process_dict.get("address"),
            display_address=process_dict.get("displayAddress"),
            e_li=process_dict.get("ELI"),
            passed=process_dict.get("passed"),
            shorten_procedure=process_dict.get("shortenProcedure"),
            urgency_status=process_dict.get("urgencyStatus"),
            urgency_withdraw_date=process_dict.get("urgencyWithdrawDate"),
            other_documents=process_dict.get("otherDocuments", []),
            rcl_num=process_dict.get("rclNum"),
            rcl_link=process_dict.get("rclLink"),
            legislative_committee=process_dict.get("legislativeCommittee"),
            principle_of_subsidiarity=process_dict.get("principleOfSubsidiarity"),
            stages=process_dict.get("stages", []),
            links=process_dict.get("links", [])    
            )
        
        session.add(process_details_db)
        session.commit()
        
        print(f"Saved process details for term {term}, number {num}")
        
        # Return full API response
        return process_dict
        
    except Exception as e:
        print(f"Error fetching process details: {e}")
        raise HTTPException(status_code=500, detail=f"Error fetching process details: {str(e)}")


#@app.post("/ai")
#async def ai_response(request: AiRequest, session: Session = Depends(get_db)):
#    result =  await ai_clarify_act(request.pos,session)
#    return {"response": result}

@app.get("/ai")
async def ai_response(pos: int, session: Session = Depends(get_db)):
    result = await ai_clarify_act(pos, session)
    return {"response": result}

@app.get("/details/{entity_id}", response_model=CombinedItem)
async def get_combined_details(
    entity_id: str,
    session: Session = Depends(get_db)
) -> CombinedItem:
    """
    Retrieve details for a single legislation act or process by its prefixed ID (e.g., 'leg-123' or 'proj-456').
    """
    if not re.match(r"^(leg|proj)-\d+$", entity_id):
        raise HTTPException(status_code=400, detail="Invalid entity_id format. Expected 'leg-XX' or 'proj-XX'.")

    entity_type, db_id_str = entity_id.split('-')
    try:
        db_id = int(db_id_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ID in entity_id. Must be an integer.")

    if entity_type == "leg":
        item = session.get(LegislationAct, db_id)
        if not item:
            raise HTTPException(status_code=404, detail=f"LegislationAct with ID {db_id} not found.")
        
        return CombinedItem(
            id=f"leg-{item.id}",
            type="legislation",
            title=item.title,
            date=item.date_created,
            status=item.status,
            description=f"Applicant: {item.applicant}",
            source_id=str(item.id),
            url=item.link,
            stages=item.stages or [],
            links=[{"href": item.link, "rel": "self"}] if item.link else [],
            sejm_id=item.sejm_id
        )
    elif entity_type == "proj":
        item = session.get(ProcessHeader, db_id)
        if not item:
            raise HTTPException(status_code=404, detail=f"ProcessHeader with ID {db_id} not found.")
        
        stages = []
        links = []
        
        if item.term:
            details = session.exec(
                select(ProcessDetails).where(
                    ProcessDetails.term == item.term,
                    ProcessDetails.number == item.number
                )
            ).first()
            
            if details:
                stages = details.stages or []
                links = details.links or []
            else:
                # Fetch from API if details not in DB
                try:
                    process_response = await get_sejm_termterm_processes_num.asyncio(
                        client=sejm_client,
                        term=item.term,
                        num=item.number
                    )
                    if process_response:
                        process_dict = process_response.to_dict()
                        # Create DB object
                        process_details_db = ProcessDetails(
                            term=process_dict.get("term"),
                            number=process_dict.get("number"),
                            title=process_dict.get("title"),
                            description=process_dict.get("description"),
                            u_e=process_dict.get("UE"),
                            document_date=process_dict.get("documentDate"),
                            change_date=process_dict.get("changeDate"),
                            web_generated_date=process_dict.get("webGeneratedDate"),
                            process_start_date=process_dict.get("processStartDate"),
                            document_type=process_dict.get("document_type"), # Use document_type
                            document_type_enum=process_dict.get("documentTypeEnum"),
                            comments=process_dict.get("comments"),
                            prints_considered_jointly=process_dict.get("printsConsideredJointly", []),
                            title_final=process_dict.get("titleFinal"),
                            closure_date=process_dict.get("closureDate"),
                            address=process_dict.get("address"),
                            display_address=process_dict.get("displayAddress"),
                            e_li=process_dict.get("ELI"),
                            passed=process_dict.get("passed"),
                            shorten_procedure=process_dict.get("shortenProcedure"),
                            urgency_status=process_dict.get("urgencyStatus"),
                            urgency_withdraw_date=process_dict.get("urgencyWithdrawDate"),
                            other_documents=process_dict.get("otherDocuments", []),
                            rcl_num=process_dict.get("rclNum"),
                            rcl_link=process_dict.get("rclLink"),
                            legislative_committee=process_dict.get("legislativeCommittee"),
                            principle_of_subsidiarity=process_dict.get("principleOfSubsidiarity"),
                            stages=process_dict.get("stages", []),
                            links=process_dict.get("links", [])    
                        )
                        session.add(process_details_db)
                        session.commit()
                        stages = process_dict.get("stages", [])
                        links = process_dict.get("links", [])
                except Exception as e:
                    print(f"Error fetching process details for {item.number}: {e}")

        return CombinedItem(
            id=f"proj-{item.id}",
            type="process",
            title=item.title or "No Title",
            date=item.change_date or item.process_start_date,
            status="Uchwalono" if item.passed else "W toku",
            description=item.description,
            source_id=str(item.id),
            url=None,
            stages=stages,
            links=links,
            term=item.term
        )
    
    raise HTTPException(status_code=400, detail="Unknown entity type.")

@app.post("/legislacja/{project_id}", response_model=LegislationAct)
async def scrape_legislation_endpoint(
    project_id: str,
    session: Session = Depends(get_db)
) -> LegislationAct:
    """
    Scrape a specific legislation project from legislative.rcl.gov.pl and save/update it in the database.
    """
    url = f"https://legislacja.rcl.gov.pl/projekt/{project_id}"
    print(f"Scraping legislation project: {url}")
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=f"Failed to fetch project page: {response.status_code}")

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Title
    title_div = soup.find('div', class_='rcl-title')
    title = title_div.get_text(strip=True) if title_div else None
    if not title:
        raise HTTPException(status_code=404, detail="Could not parse title from project page")

    # Info rows
    info_div = soup.find('div', class_='info')
    applicant = None
    date_created = None
    date_modified = None
    status = None
    category_id = None
    number = None

    if info_div:
        rows = info_div.find_all('div', class_='row', recursive=False)
        for row in rows:
            text = row.get_text(" ", strip=True)
            if "Wnioskodawca:" in text:
                applicant = text.replace("Wnioskodawca:", "").strip()
            elif "Data utworzenia:" in text:
                date_str = text.replace("Data utworzenia:", "").strip()
                try:
                    date_created = datetime.strptime(date_str, "%d-%m-%Y")
                except ValueError:
                    pass
            elif "Data modyfikacji:" in text:
                date_str = text.replace("Data modyfikacji:", "").strip()
                try:
                    date_modified = datetime.strptime(date_str, "%d-%m-%Y")
                except ValueError:
                    pass
            elif "Status projektu:" in text:
                status = text.replace("Status projektu:", "").strip()
            elif "Działy:" in text:
                link = row.find('a', href=re.compile(r'deptId='))
                if link:
                    href = link['href']
                    match = re.search(r'deptId=(\d+)', href)
                    if match:
                        category_id = int(match.group(1))
    
    # Number extraction
    labels = soup.find_all('div', class_='text-right')
    for label in labels:
        if "Numer" in label.get_text():
            value_div = label.find_next_sibling('div')
            if value_div:
                number = value_div.get_text(strip=True)
                break
    
    if category_id is None:
        category_id = 0 # Default or unknown

    # Stage extraction
    stages = []
    sejm_id = None
    timeline_elements = soup.find_all('div', class_=['cbp_tmlabel', 'cbp_tmlabel_notstart'])

    for element in timeline_elements:
        stage_data = {"name": None, "url": None, "date_modified": None}
        
        stage_text = None
        # Try to find a link (<a> tag) for the stage name
        link_elem = element.find('a', string=re.compile(r"^\s*\d+\.\s*.*"))
        if link_elem:
            stage_text = link_elem.get_text(strip=True)
            stage_data["url"] = BASE_URL + link_elem['href'] if link_elem.get('href') else None
        else:
            # If no link, look for a direct text node (NavigableString) that matches the pattern
            # This searches recursively within the 'element'
            numbered_text_node = element.find(string=re.compile(r"^\s*\d+\.\s*.*"))
            if numbered_text_node:
                stage_text = str(numbered_text_node).strip()
        
        if stage_text:
            match = re.match(r"^\d+\.\s*(.*)", stage_text)
            if match:
                stage_data["name"] = match.group(1).strip()
        
        # Look for the date (always in <div class="small2">)
        date_element = element.find('div', class_='small2')
        if date_element:
            date_str = date_element.get_text(strip=True).replace("Data ostatniej modyfikacji:", "").strip()
            try:
                stage_data["date_modified"] = datetime.strptime(date_str, "%d-%m-%Y").isoformat()
            except ValueError:
                pass
        
        # Extract sejm_id (RM-xxxx) from any text within the entire cbp_tmlabel element
        if not sejm_id:
            full_element_text = element.get_text()
            sejm_id_match = re.search(r"(RM-\d+-\d+-\d+)", full_element_text)
            if sejm_id_match:
                sejm_id = sejm_id_match.group(1)

        if stage_data["name"]: # Only add if a name was found
            stages.append(stage_data)

    # NEW: sejm_id extraction from specific link
    sejm_id = None
    sejm_link_element = soup.find('a', href=re.compile(r"sejm\.gov\.pl.*(RM-\d+-\d+-\d+)"))
    if sejm_link_element:
        href = sejm_link_element['href']
        sejm_id_match = re.search(r"(RM-\d+-\d+-\d+)", href)
        if sejm_id_match:
            sejm_id = sejm_id_match.group(1)

    # Upsert
    existing = session.exec(select(LegislationAct).where(LegislationAct.link == url)).first()
    if existing:
        existing.title = title
        existing.applicant = applicant
        existing.number = number
        existing.date_created = date_created
        existing.date_modified = date_modified
        existing.status = status
        existing.category_id = category_id
        existing.stages = stages
        existing.sejm_id = sejm_id
        session.add(existing)
        session.commit()
        session.refresh(existing)
        return existing
    else:
        act = LegislationAct(
            title=title,
            applicant=applicant,
            number=number,
            date_created=date_created,
            date_modified=date_modified,
            link=url,
            status=status,
            category_id=category_id,
            stages=stages,
            sejm_id=sejm_id
        )
        session.add(act)
        session.commit()
        session.refresh(act)
        return act
