from fastapi import APIRouter, Depends, HTTPException
from google import genai
from dotenv import load_dotenv
from sqlmodel import Session, select

from app.models.models import ActInfo

load_dotenv()

router = APIRouter(prefix="/ai", tags=["AI"])

def ai_clarify_act(pos: int, session: Session):
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