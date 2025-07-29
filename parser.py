from bs4 import BeautifulSoup

class Parser:
    def parse_books(self, html):
        soup = BeautifulSoup(html, "lxml")
        books = []

        for item in soup.select(".product_pod"):
            title = item.h3.a["title"]

            raw_price = item.select_one(".price_color").text
            price = raw_price.replace("£", "").replace("Â", "").strip()
            price = price.replace("\xa0", "")  
            try:
                price = float(price)
            except ValueError:
                price = None  

            rating = item.p["class"][1]

            books.append({
                "title": title,
                "price": price,
                "rating": rating
            })

        return books
