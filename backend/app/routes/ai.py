from fastapi import APIRouter
from google import genai
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/ai", tags=["AI"])

def ai_test_function():
    """Function to test AI generation"""
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents="Explain how AI works in a few words"
    )
    return response.text

@router.get("/test")
def ai_test_endpoint():
    """Endpoint to test AI generation"""
    result = ai_test_function()
    return {"response": result}