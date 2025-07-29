from scraper import Scraper
from parser import Parser
from storage import Storage
from utils import log

def main():
    log("🚀 Starting Book Scraper")
    scraper = Scraper()
    parser = Parser()
    storage = Storage()

    total_pages = scraper.get_total_pages()
    all_books = []

    for page in range(1, total_pages + 1):
        html = scraper.fetch_page(page)
        if html:
            books = parser.parse_books(html)
            log(f"📦 Page {page}: {len(books)} books scraped")
            all_books.extend(books)

    storage.save_to_csv(all_books)
    log("🎉 Scraping Completed!")

if __name__ == "__main__":
    main()
