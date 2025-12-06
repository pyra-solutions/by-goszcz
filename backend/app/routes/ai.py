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


@router.post("/clarify/{act_id}")
def ai_clarify_act(pos: int, session: Session = Depends(get_db)):
    """Use AI to clarify an act from database"""
    
    # Get act from database using ORM
    act = session.get(Main, act_id)  # zmień Hero na Act
    
    if not act:
        raise HTTPException(status_code=404, detail="Act not found")
    
    # Use AI to clarify
    client = genai.Client()
    prompt = f"Wyjaśnij ten akt prawny w prostych słowach zrozumiałych dla osób niezwizanych z środowiskiem prawniczym: {act.tytul}"
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite", 
        contents=prompt
        #config={
        #    "response_mime_type": "application/json",
        #    "response_json_schema": Recipe.model_json_schema(),
        #}
    )
    
    return {
        "act": act,
        "clarification": response.text
    }
