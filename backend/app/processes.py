import asyncio
from clientsejm.client import Client
from clientsejm.api.processes import get_sejm_termterm_processes
from clientsejm.models.process_header import ProcessHeader as ProcessHeaderAPI

from sqlmodel import SQLModel, Session

from models.models import ProcessHeader
from database import engine

async def fetch_all_processes(client: Client, term: int) -> list[ProcessHeaderAPI]:
    """
    Fetches all processes for a given term using pagination.
    """
    all_processes = []
    offset = 0
    limit = 100
    
    print(f"Fetching processes for term: {term}")
    
    has_more = True
    while has_more:
        processes_response = await get_sejm_termterm_processes.asyncio(
            client=client,
            term=term,
            offset=offset,
            limit=limit
        )
        
        if not processes_response:
            has_more = False
            break
        
        print(f"  - Fetched {len(processes_response)} processes (offset: {offset})")
        all_processes.extend(processes_response)
        
        # Check if we got fewer results than the limit (last page)
        if len(processes_response) < limit:
            has_more = False
        else:
            offset += limit
    
    return all_processes

async def main():
    """
    Downloads all processes from the API and saves them to the database.
    """
    client = Client(base_url="https://api.sejm.gov.pl/", timeout=20.0)

    SQLModel.metadata.create_all(engine)
    session = Session(engine)

    # Fetch all processes for term 10
    processes = await fetch_all_processes(client, term=30)
    
    if not processes:
        print("No processes found.")
        return
    
    print(f"\nTotal processes fetched: {len(processes)}")
    print("Saving to database...")
    for i,process_api in enumerate(processes, 1):
        process_dict = process_api.to_dict()
        print(process_dict)
        
        process_db = ProcessHeader(
            #id=None,
            #u_e=process_dict.get("ue"),
            #e_li=process_dict.get("ELI"),
            term=process_dict.get("term"),#
            number=process_dict.get("number"),#
            title=process_dict.get("title"),#
            title_final=process_dict.get("titleFinal"),#
            description=process_dict.get("description"),
            ue=process_dict.get("ue"),
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
        
        # Commit every 100 records
        if i % 10 == 0:
            session.commit()
            print(f"  Progress: {i}/{len(processes)} processes saved")
    
    session.commit()
    session.close()
    print(f"Saved {len(processes)} processes to database")

if __name__ == "__main__":
    asyncio.run(main())