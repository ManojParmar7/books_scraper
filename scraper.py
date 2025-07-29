import requests
from bs4 import BeautifulSoup
from config import BASE_URL, HEADERS
from utils import log

class Scraper:
    def get_total_pages(self):
        """Automatically detect total pages from site"""
        html = requests.get(BASE_URL.format(1), headers=HEADERS).text
        soup = BeautifulSoup(html, "lxml")
        total_text = soup.find('li', class_='current').get_text(strip=True)
        total = int(total_text.split()[-1])  # “Page 1 of 50” → 50
        log(f"📄 Total pages detected: {total}")
        return total

    def fetch_page(self, page_number):
        """Fetch HTML content for a page"""
        url = BASE_URL.format(page_number)
        log(f"🌐 Fetching page: {url}")
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            return response.text
        else:
            log(f"❌ Failed with status {response.status_code}")
            return None
