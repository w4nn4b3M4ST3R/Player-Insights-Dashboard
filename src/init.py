import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_player_stats(player_url, player_name):
    response = requests.get(player_url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    stats = {}
    tables = soup.find_all('table')
    for table in tables:
        caption = table.find("caption")
        header = table.find("th", colspan="2")

        title = ""
        if caption and caption.get_text(strip=True):
            title = caption.get_text(strip=True)
        elif header and header.get_text(strip=True):
            title = header.get_text(strip=True)

        rows = table.find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            if len(cols) == 2:
                label = cols[0].get_text(" ", strip=True).replace(":", "")
                value = cols[1].get_text(" ", strip=True)
                if label or value:
                    stats[f"{player_name} {title} - {label}"] = value
    return stats

def process_stat_value(value):
    if pd.isna(value) or value == '' or value == '-':
        return None
    try:
        str_value = str(value).strip().replace('%', '').replace(',', '').replace('$', '')
        return float(str_value) if str_value else None
    except (ValueError, TypeError):
        return None