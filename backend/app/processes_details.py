import asyncio
from clientsejm.client import Client
from clientsejm.api.processes import get_sejm_termterm_processes_num
from clientsejm.models.process_details import ProcessDetails as ProcessDetailsAPI

from sqlmodel import SQLModel, Session, select

from models.models import ProcessDetails, ProcessHeader
from database import engine

async def fetch_process_details(client: Client, term: int, num: str) -> ProcessDetailsAPI:
    """
    Fetches process details for a given term and process number.
    """
    print(f"  - Fetching details for term {term}, number {num}")
    
    process_response = await get_sejm_termterm_processes_num.asyncio(
        client=client,
        term=term,
        num=num
    )
    
    return process_response

async def main():
    """
    Downloads all process details from the API based on ProcessHeader table
    and saves them to the database.
    """
    client = Client(base_url="https://api.sejm.gov.pl/", timeout=30.0)

    SQLModel.metadata.create_all(engine)
    session = Session(engine)

    # Get all processes from ProcessHeader
    query = select(ProcessHeader)
    processes = session.exec(query).all()
    
    if not processes:
        print("No processes found in ProcessHeader table.")
        return
    
    print(f"Found {len(processes)} processes in database")
    print("Fetching process details...\n")
    
    saved_count = 0
    skipped_count = 0
    error_count = 0
    
    for i, process in enumerate(processes, 1):
        # Check if details already exist
        existing = session.exec(
            select(ProcessDetails).where(
                ProcessDetails.term == process.term,
                ProcessDetails.number == process.number
            )
        ).first()
        
        if existing:
            skipped_count += 1
            print(f"[{i}/{len(processes)}] Already exists: term {process.term}, number {process.number}")
            continue
        
        try:
            # Fetch from API
            process_api = await fetch_process_details(client, process.term, process.number)
            
            if not process_api:
                print(f"[{i}/{len(processes)}] No response for term {process.term}, number {process.number}")
                error_count += 1
                continue
            
            process_dict = process_api.to_dict()
            
            # Create ProcessDetails instance
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
            saved_count += 1
            
            # Commit every 10 records
            if i % 10 == 0:
                session.commit()
                print(f"[{i}/{len(processes)}] Progress saved - Total saved: {saved_count}")
            
            print(f"[{i}/{len(processes)}] Saved: term {process.term}, number {process.number}")
            
            # Small delay to avoid overwhelming the API
            await asyncio.sleep(0.5)
            
        except Exception as e:
            error_count += 1
            print(f"[{i}/{len(processes)}] Error for term {process.term}, number {process.number}: {e}")
            continue
    
    # Final commit
    session.commit()
    session.close()
    

    print(f"Completed:")
    print(f"  Total processes: {len(processes)}")
    print(f"  Saved: {saved_count}")
    print(f"  Skipped (already in DB): {skipped_count}")
    print(f"  Errors: {error_count}")


if __name__ == "__main__":
    asyncio.run(main())