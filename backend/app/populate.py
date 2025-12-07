import asyncio
import httpx
from sqlmodel import Session, select
from app.database import engine
from app.models.models import ProcessDetails

async def populate_process_details():
    """
    Script to populate process details for term 10, numbers 1-1000
    Only fetches if not already in database
    """
    base_url = "http://localhost:8000"  # Adjust if your API runs on different port
    term = 10
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        for num in range(1, 1001):
            # Check if already exists in database
            with Session(engine) as session:
                existing = session.exec(
                    select(ProcessDetails).where(
                        ProcessDetails.term == term,
                        ProcessDetails.number == str(num)
                    )
                ).first()
                
                if existing:
                    print(f"Process {num} already exists, skipping...")
                    continue
            
            # If not exists, call API endpoint
            try:
                print(f"Fetching process {num} for term {term}...")
                response = await client.get(f"{base_url}/term{term}/processes/{num}")
                
                if response.status_code == 200:
                    print(f"✓ Successfully fetched process {num}")
                elif response.status_code == 404:
                    print(f"✗ Process {num} not found (404)")
                else:
                    print(f"✗ Error fetching process {num}: {response.status_code}")
                    
            except Exception as e:
                print(f"✗ Exception fetching process {num}: {str(e)}")
            
            # Small delay to avoid overwhelming the API
            await asyncio.sleep(0.5)

if __name__ == "__main__":
    print("Starting to populate process details for term 10, numbers 1-1000...")
    asyncio.run(populate_process_details())
    print("Done!")