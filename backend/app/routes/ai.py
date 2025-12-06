from fastapi import APIRouter, Depends, HTTPException
from google import genai
from dotenv import load_dotenv
from sqlmodel import Session, select
import httpx
import PyPDF2
from io import BytesIO
from pydantic import BaseModel
from typing import List

from app.database import get_db
from app.models.models import ActInfo

load_dotenv()

router = APIRouter(prefix="/ai", tags=["AI"])


class ActSummary(BaseModel):
    main_topic: str
    key_points: List[str]
    affected_parties: List[str]
    summary: str


async def ai_clarify_act(pos: int, session: Session):
    """
    Pobiera dane z bazy według modelu ActInfo dla podanego pos,
    parsuje PDF z API Sejmu i analizuje go przez Gemini
    """
    genai_client = genai.Client()

    statement = select(ActInfo).where(ActInfo.pos == pos)
    act = session.exec(statement).first()
    
    if not act:
        raise HTTPException(status_code=404, detail=f"Act with pos={pos} not found")
    
    if not act.eli:
        raise HTTPException(status_code=404, detail=f"Act with pos={pos} has no ELI")
    
    # Pobierz PDF z API Sejmu
    pdf_url = f"https://api.sejm.gov.pl/eli/acts/{act.eli}/text.pdf"
    
    async with httpx.AsyncClient(timeout=90.0) as http_client:
        response = await http_client.get(pdf_url)
        
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail=f"PDF not found for ELI: {act.eli}, URL {pdf_url}")
        
        # Parsuj PDF
        pdf_file = BytesIO(response.content)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Wyciągnij tekst ze wszystkich stron
        text_content = ""
        for page in pdf_reader.pages:
            text_content += page.extract_text() + "\n"
    
    # Wyślij do Gemini
    prompt = f"""
    Przeanalizuj poniższy akt prawny i wyciągnij najważniejsze informacje.
    Tytuł aktu: {act.title}
    
    Treść aktu:
    {text_content.strip()}
    
    Proszę o zwięzłe i proste podsumowanie tego aktu prawnego w języku polskim.
    """
    
    gemini_response = genai_client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": ActSummary.model_json_schema(),
        },
    )
    
    return {
        "id": act.id,
        "eli": act.eli,
        "title": act.title,
        "pos": act.pos,
        "pdf_url": pdf_url,
        "analysis": gemini_response.text
    }