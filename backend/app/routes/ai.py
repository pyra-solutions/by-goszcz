from fastapi import APIRouter, Depends, HTTPException
from google import genai
from dotenv import load_dotenv
from sqlmodel import Session, select

from app.database import get_db

load_dotenv()

router = APIRouter(prefix="/ai", tags=["AI"])

def ai_test_function():
    """Function to test AI generation"""
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite", contents="Explain how AI works in a few words"
    )
    return response.text


    """
    Pobiera dane z bazy według modelu ActInfo dla podanego pos
    """
    statement = select(ActInfo).where(ActInfo.pos == pos)
    act = session.exec(statement).first()
    
    if not act:
        raise HTTPException(status_code=404, detail=f"Act with pos={pos} not found")
    
    return {
        "id": act.id,
        "eli": act.eli,
        "title": act.title,
        "address": act.address,
        "publisher": act.publisher,
        "year": act.year,
        "volume": act.volume,
        "pos": act.pos,
        "display_address": act.display_address,
        "promulgation": act.promulgation,
        "status": act.status,
        "act_type": act.act_type
    }