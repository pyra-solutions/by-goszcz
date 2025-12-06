import asyncio
import time
from eli_for_polish_acts_client.client import Client
from eli_for_polish_acts_client.api.listing_acts import get_years, get_acts_in_year, get_publishers
from eli_for_polish_acts_client.api.act_details import get_act_pdf
from eli_for_polish_acts_client.models.act_info import ActInfo as ActInfoAPI
import os

from sqlalchemy import engine
from sqlmodel import SQLModel, Session

from models.models import ActInfo
from database import engine

async def download_act(semaphore: asyncio.Semaphore, client: Client, act: ActInfoAPI):
    """
    Downloads a single act.
    """
    file_path = os.path.join("../data/acts/", f"{act.publisher}_{act.year}_{act.pos}.pdf")
    if os.path.exists(file_path):
        print(f"  - Already downloaded {act.address}")
        return

    print(act)

    async with semaphore:
        try:
            print(f"  - Attempting to download {act.address}")
            start_download_time = time.time()
            pdf_response = await get_act_pdf.asyncio_detailed(
                client=client,
                publisher=act.publisher,
                year=act.year,
                position=act.pos,
            )
            end_download_time = time.time()

            if pdf_response.content:
                with open(file_path, "wb") as f:
                    f.write(pdf_response.content)
                print(f"    - Saved to {file_path} in {int((end_download_time - start_download_time) * 1000)} ms")
            else:
                print(f"    - Could not download {act.address}")
        except Exception as e:
            print(f"    - Error downloading {act.address}: {e}")

async def main():
    """
    Downloads all acts from the API concurrently, with persistence.
    """
    FROM = 2024
    TO = 2025
    start_time = time.time()
    client = Client(base_url="https://api.sejm.gov.pl/eli", timeout=20.0)
    semaphore = asyncio.Semaphore(30)
    tasks = []

    SQLModel.metadata.create_all(engine)
    session =  Session(engine)

    publishers_response = await get_publishers.asyncio(client=client)
    if not publishers_response:
        print("Could not fetch publishers.")
        return
    publishers_data = [p.to_dict() for p in publishers_response]

    for publisher_data in publishers_data:
        publisher_code = publisher_data["code"]
        print(f"Fetching for publisher: {publisher_code}")

        years_response = await get_years.asyncio(client=client, publisher=publisher_code)
        if not years_response:
            print(f"Could not fetch years for publisher: {publisher_code}")
            continue
        years_data = years_response.to_dict()
        
        for year in years_data["years"]:
            if not (FROM <= year and year >= TO):
                continue
            print(f"Fetching acts for year: {year}")

            acts_response = await get_acts_in_year.asyncio(
                client=client,
                year=year,
                publisher=publisher_code
            )
            if not acts_response:
                print(f"No acts found for year: {year}")
                continue
            acts_data = acts_response.to_dict()
            
            for act_data in acts_data["items"]:
                print(act_data)
                act = ActInfoAPI.from_dict(act_data)

                
                act_dict = {
                "id": 0,
                "address":act.address,
                "publisher":act.publisher,
                "year":act.year,
                "volume":act.volume,
                "pos":act.pos,
                "title":act.title,
                "display_address":act.display_address,
                "promulgation":act.promulgation,
                "announcement_date":act.announcement_date,
                "text_pdf":act.text_pdf,
                "text_html":act.text_html,
                "change_date":act.change_date,
                "eli":act.eli,
                "act_type":act.type_,
                "status":act.status,
                }


                act = ActInfo.model_validate(act_dict)
                act.id = None
                session.add(act)
                print("ADDED!")
                
                task = asyncio.create_task(download_act(semaphore, client, ActInfoAPI.from_dict(act_data)))
                tasks.append(task)

            session.commit()

    await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Total time taken: {int((end_time - start_time) * 1000)} ms")

if __name__ == "__main__":
    asyncio.run(main())
