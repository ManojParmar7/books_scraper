# 📚 Books Scraper

This project is a **Python web scraper** that collects **book details** (Title, Price, and Rating) from [BooksToScrape.com](http://books.toscrape.com) – a site built for web scraping practice.

## 🚀 Features
✅ Scrapes **all pages** automatically (no hardcoding page numbers)  
✅ Extracts **book title, price (clean float), and rating**  
✅ Saves data into **CSV** format  
✅ Modular code structure (scraper, parser, storage, utils) for easy maintenance  

## 📂 Project Structure
books_scraper/
│── main.py # Main entry point
│── scraper.py # Handles requests and pagination
│── parser.py # Extracts data from HTML
│── storage.py # Saves data to CSV
│── utils.py # Helper functions (logging etc.)
│── config.py # Config (Base URL, Headers, CSV filename)
│── requirements.txt # Python dependencies
└── data/
└── books.csv # Scraped data output


## 🛠 Tech Stack
- **Python 3.9+**
- **Requests** – for fetching web pages
- **BeautifulSoup4 (bs4)** – for parsing HTML
- **Pandas** – for saving to CSV

## ⚙️ Setup & Installation

1️⃣ Clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/books_scraper.git
cd books_scraper
