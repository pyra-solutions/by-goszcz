from bs4 import BeautifulSoup
from datetime import datetime
import requests
from sqlmodel import SQLModel, Session

from database import engine

from models.models import Consultation

res = ""
with open("konsultacje_index_example.html")  as index_html:
    res = index_html.read()

soup = BeautifulSoup(res,features="html.parser")

tables = soup.find_all("table", class_="tab proj")

if len(tables) != 1:
    raise Exception("no project table found")

table = tables[0]


from datetime import datetime

consultations: list[Consultation] = []

for row_index, child in enumerate(table.tbody.children):
    tds = [x for x in child if getattr(x, "name", None) == "td"]

    if len(tds) != 4:
        raise Exception("not enough tds")

    consultation = Consultation()

    submission_raw = tds[0].nobr.get_text(strip=True)
    consultation.submission_date = datetime.strptime(submission_raw, "%Y-%m-%d")

    consultation.project_name = tds[1].a.strong.get_text(strip=True)

    next_is_publisher = False
    is_dotyczy = False
    description = ""
    for idx, el in enumerate(tds[1]):
        if next_is_publisher:
            consultation.publisher = getattr(el, "text", str(el)).strip()
            next_is_publisher = False

        if str(el.text).strip() == "Wnioskodawca":
            next_is_publisher = True
        if str(el.text).strip() == "Dotyczy":
            is_dotyczy = True

        if is_dotyczy:
            description+=str(el)

        if idx == 6:
            # el is likely a NavigableString or tag; convert to text
            consultation.consultation_id = getattr(el, "text", str(el)).strip()
    consultation.description = description
    print(consultation.description)

    for idx, el in enumerate(tds[2]):
        text = getattr(el, "text", "").strip()

        if idx == 0:
            consultation.start_date = datetime.strptime(text, "%Y-%m-%d")

        if idx == 3:
            consultation.end_date = datetime.strptime(text, "%Y-%m-%d")

    for idx, el in enumerate(tds[3]):
        raw = getattr(el, "text", "").strip()

        if idx == 0:
            if raw == "Konsultacje zakończone":
                consultation.status = "finished"
            else:
                consultation.status = "in_progress"

        if idx == 5:
            # "Liczba ankiet: X"
            if "Liczba ankiet:" in raw:
                consultation.poll_amount = int(raw.split("Liczba ankiet: ")[1])

        if idx == 8:
            # <a href="?pos=1234">
            if hasattr(el, "a") and "href" in el.a.attrs:
                consultation.project_pos = int(el.a["href"].split("=")[1])

    consultations.append(consultation)

with Session(engine) as session:
    SQLModel.metadata.create_all(engine)
    session =  Session(engine)
    session.add_all(consultations)
    session.commit()

import requests

url = "https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=KONSULTACJE_KOMENTARZE&NrProjektu=RPW/34468/2025&Typ=ALL"

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "referer": "https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=KONSULTACJE_WYNIKI&NrProjektu=RPW/34468/2025",
    "sec-ch-ua": '"Not_A Brand";v="99", "Chromium";v="142"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
}


cookies = {
    cookie.split("=",1)[0]: cookie.split("=",1)[1]
    for cookie in (
'f5_cspm=1234; visid_incap_3077746=O1SOACpERuOXmfWLoUzgMg0ZNGkAAAAAQUIPAAAAAADq140ND2Wl4ky1fCfq9OpB; visid_incap_3078757=x6f4KpVMTySjDgTvgEn2qORqNGkAAAAAQUIPAAAAAAB6PvLhtlIlzg1NZSu0qEul; visid_incap_3054990=95DZgSmGQZacYsJFT1AyL/VnIGkAAAAAQkIPAAAAAACA4N/AAbyShuFZ18p5ylVzhy92EcBKA+99; incap_wafapi_sh_3054990=rflTRZBvTOGVjQ0i7tZInZ54NGkAAAAAQUIPAAAAAACA4N/AAbyShuFvg5z6pmWZqhV/BcJxrhsw; SessionID=36471BA218A204F265691BA31B8A8A752E954AF3; incap_ses_520_3054990=8K+XBbyqrHqNcjm5b2k3BzWTNGkAAAAA8aK0aqFGz1/i9nUOnLtwaw==; incap_ses_519_3078757=2U/1P/a2FhyvuopCJNwzB7yXNGkAAAAATzR9kazcASlqcp3Ed8qv8g==; TS0157497f=01ef84482e4d36174b17b16b61db33dfafa801b0d5560f95f37b21cfd78bf58ce872f3bf46443828b21f7d873fb1c6428abfcf14ab66a5d76ebb9412a6c4be41baf3831e2284f3a35cc71913b1516e74be48f5ad6a6d9a1f03823bf7b59dbaf140f69c3424; TSa8269e27029=08a02c1a15ab28007416f12fd83aa7c8008dd06fb3b6cc60df5209140c5354e8546eb1baf0756e081c6d4a030c09853a; TSa8269e27077=08a02c1a15ab2800344b384adcc9bbb45a3cf4a85861d65ce2cfbf1a32e9e829449ab22cdbcfada878f67afe6b9bd7330830492d39172000c0c59b8e08929a61f9cf1e4681acc0db22eb4af5468d0fc5285f5f96f4702d9f; TS00000000076=08a02c1a15ab2800d8981d538e7521ab92820c06a88b311df533befbadad81421025149403f95a6ca513a801025eca7008e55da97409d000d4e10ec0b07573b6aa87c4f15bfaaac7cd68ae150931648885276e02c122938ff0c6d76aee96e8a0847328d7083bedb73dc31e7c49138c6529b464302bf2ead3872645023202912e7f6a83d024b0c594a241cea2684fb2bec0a91ac6541f6d8c467b450b6bcfdf9382286f92e54b58ad846d507788111db2904feb9cc2a8326052a678162cf9af7e684d7a86096ef384ce2675a6b2c0020b99c059ad6c7918a09b283d5c842b2bd06c6ba66aa965b0c69c940d39292625837c5094e6c8589384290e1b1983a541e3dd1e77f7aeaef9db; TSPD_101_DID=08a02c1a15ab2800d8981d538e7521ab92820c06a88b311df533befbadad81421025149403f95a6ca513a801025eca7008e55da974063800c80137fae6dd473ec64f5df87354ff7704b4782bff86432f208f6a98a88934d4c42f378ea6c0b06b8e59db6ae436e91a36ebf976cc136112; TSPD_101=08a02c1a15ab2800357463951e859d378157afe398e168c88062f989131800bb2e48c3950be4fdc64c9930551ce3be950872e5649d0518003bf0155a14586cdc516dc8c9b1f6565c28a28593703239b5; TSb86c9039027=08a02c1a15ab20005cead215f99507bd74e9898e45e09eab06cd71b2f3e31efb5d9c651e83ed5c9d08de83516a113000a8dc3b108f9030ac07a7b4d9a658bceaf9f426dc51596033ac3c8890164d7a98f27f03bb20843e3ce90c833706cbd64f'
    ).split("; ")
}


import requests
from itertools import cycle

def load_proxies(path="proxies.txt"):
    proxies = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            ip, port, user, password = line.split(":")
            proxy_url = f"http://{user}:{password}@{ip}:{port}"
            proxies.append({
                "http": proxy_url,
                "https": proxy_url,
            })
    return proxies


proxy_list = load_proxies("proxies.txt")
proxy_cycle = cycle(proxy_list)


def fetch_with_proxy(url, headers, cookies, max_attempts=10):
    """
    Try multiple proxies until:
    - success
    - or max_attempts exhausted
    """

    attempt = 0

    while attempt < max_attempts:
        proxy = next(proxy_cycle)
        attempt += 1

        try:
            res = requests.get(
                url,
                headers=headers,
                cookies=cookies,
                proxies=proxy,
                timeout=20
            )

            text_lower = res.text.lower()

            # CAPTCHA detection
            if "captcha" in text_lower or "catpcha" in text_lower:
                print(f"[!] CAPTCHA detected — retrying with next proxy...")
                continue

            if res.status_code != 200:
                print(f"[!] Bad status {res.status_code} — retrying with next proxy...")
                continue

            print(f"[+] Success with proxy {proxy['http']}")
            return res

        except Exception as e:
            print(f"[!] Proxy failed ({proxy['http']}): {e}")
            continue

    print("[X] All proxies failed or CAPTCHA every time.")
    return None

import os

for consultation in consultations:
    filename = f"consultations/{consultation.consultation_id.replace('/', '_')}.html"

    # --- SKIP IF FILE ALREADY EXISTS ---
    if os.path.exists(filename):
        print(f"[SKIP] {filename} already exists")
        continue

    url = (
        f"https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp"
        f"?symbol=KONSULTACJE_KOMENTARZE"
        f"&NrProjektu={consultation.consultation_id}"
        f"&Typ=ALL"
    )

    res = fetch_with_proxy(url, headers=headers, cookies=cookies)

    if not res:
        print("Failed to fetch, skipping.")
        continue

    # ensure the directory exists
    os.makedirs("consultations", exist_ok=True)

    with open(filename, "w+", encoding="utf-8") as f:
        f.write(res.text)

    print("-> saved", filename)

