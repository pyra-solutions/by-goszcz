import asyncio
import time
import json
from eli_for_polish_acts_client.client import Client
from eli_for_polish_acts_client.api.listing_acts import get_years, get_acts_in_year, get_publishers
from eli_for_polish_acts_client.api.act_details import get_act_pdf
from eli_for_polish_acts_client.models.act_info import ActInfo
import os

async def download_act(semaphore: asyncio.Semaphore, client: Client, act: ActInfo):
    """
    Downloads a single act.
    """
    file_path = os.path.join("acts", f"{act.publisher}_{act.year}_{act.pos}.pdf")
    if os.path.exists(file_path):
        print(f"  - Already downloaded {act.address}")
        return

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


async def download_year(year: int):
    client = Client(base_url="https://api.sejm.gov.pl/eli", timeout=20.0)
    semaphore = asyncio.Semaphore(30)
    tasks = []

    # Publishers
    publishers_file = "api_responses/publishers.json"
    if os.path.exists(publishers_file):
        with open(publishers_file, "r") as f:
            publishers_data = json.load(f)
    else:
        publishers_response = await get_publishers.asyncio(client=client)
        if not publishers_response:
            print("Could not fetch publishers.")
            return
        publishers_data = [p.to_dict() for p in publishers_response]
        with open(publishers_file, "w") as f:
            json.dump(publishers_data, f)

    for publisher_data in publishers_data:
        publisher_code = publisher_data["code"]
        print(f"Fetching for publisher: {publisher_code}")

        # Years
        years_file = f"api_responses/years/{publisher_code}.json"
        if os.path.exists(years_file):
            with open(years_file, "r") as f:
                years_data = json.load(f)
        else:
            years_response = await get_years.asyncio(client=client, publisher=publisher_code)
            if not years_response:
                print(f"Could not fetch years for publisher: {publisher_code}")
                continue
            years_data = years_response.to_dict()
            os.makedirs(os.path.dirname(years_file), exist_ok=True)
            with open(years_file, "w") as f:
                json.dump(years_data, f)
        
        for year in years_data["years"]:
            print(f"Fetching acts for year: {year}")

            # Acts
            acts_dir = f"api_responses/acts/{publisher_code}"
            os.makedirs(acts_dir, exist_ok=True)
            acts_file = f"{acts_dir}/{year}.json"

            if os.path.exists(acts_file):
                with open(acts_file, "r") as f:
                    acts_data = json.load(f)
            else:
                acts_response = await get_acts_in_year.asyncio(
                    client=client,
                    year=year,
                    publisher=publisher_code
                )
                if not acts_response:
                    print(f"No acts found for year: {year}")
                    continue
                acts_data = acts_response.to_dict()
                with open(acts_file, "w") as f:
                    json.dump(acts_data, f)
            
            for act_data in acts_data["items"]:
                task = asyncio.create_task(download_act(semaphore, client, ActInfo.from_dict(act_data)))
                tasks.append(task)

async def main():
    """
    Downloads all acts from the API concurrently, with persistence.
    """

    await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Total time taken: {int((end_time - start_time) * 1000)} ms")

if __name__ == "__main__":
    asyncio.run(main())
