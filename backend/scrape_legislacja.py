import sys
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from sqlmodel import Session, select, SQLModel

# Add current directory to path to import app modules
sys.path.append(os.getcwd())

try:
    from app.database import engine
    from app.models.models import LegislationAct
except ImportError:
    # Try alternate import if running from root
    from backend.app.database import engine
    from backend.app.models.models import LegislationAct

BASE_URL = "https://legislacja.rcl.gov.pl"

def parse_date(date_str):
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str.strip(), "%d-%m-%Y")
    except ValueError:
        return None

def scrape_category(dept_id, session):
    # Using pSize=10 to fetch at least 5 items without overloading
    url = f"{BASE_URL}/lista?pSize=10&deptId={dept_id}"
    
    print(f"Scraping category {dept_id}...")
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        if response.status_code != 200:
            print(f"Failed to fetch {url}: {response.status_code}")
            return

        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')
        if not table:
            print(f"No table found for category {dept_id}")
            return

        rows = table.find_all('tr')
        # Skip header
        data_rows = rows[1:]
        
        count = 0
        for row in data_rows:
            if count >= 5:
                break
            
            cols = row.find_all('td')
            if len(cols) < 5:
                continue
            
            # 1. Title & Link
            title_col = cols[0]
            link_tag = title_col.find('a')
            if not link_tag:
                continue
            title = link_tag.get_text(strip=True)
            link_href = link_tag.get('href')
            
            if link_href.startswith('/'):
                link = BASE_URL + link_href
            else:
                link = link_href
            
            # 2. Applicant
            applicant_col = cols[1]
            applicant = applicant_col.get_text(strip=True)
            
            # 3. Number
            number_col = cols[2]
            number = number_col.get_text(strip=True)
            
            # 4. Date Created
            date_created_col = cols[3]
            date_created = parse_date(date_created_col.get_text(strip=True))
            
            # 5. Date Modified
            date_modified_col = cols[4]
            date_modified = parse_date(date_modified_col.get_text(strip=True))
            
            # Upsert logic
            existing = session.exec(select(LegislationAct).where(LegislationAct.link == link)).first()
            if existing:
                existing.title = title
                existing.applicant = applicant
                existing.number = number
                existing.date_created = date_created
                existing.date_modified = date_modified
                existing.category_id = dept_id
                session.add(existing)
            else:
                act = LegislationAct(
                    title=title,
                    applicant=applicant,
                    number=number,
                    date_created=date_created,
                    date_modified=date_modified,
                    link=link,
                    category_id=dept_id
                )
                session.add(act)
            
            count += 1
        
        session.commit()
        print(f"Saved {count} acts for category {dept_id}")
        
    except Exception as e:
        print(f"Error scraping category {dept_id}: {e}")

def main():
    # Create tables if they don't exist
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        for i in range(36): # 0 to 35 inclusive
            scrape_category(i, session)

if __name__ == "__main__":
    main()
