
import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.parse import urljoin

# Step 1: Website URL
url = "https://books.toscrape.com/"

# Step 2: Store all scraped data
data = []
seen_titles = set()

# Step 3: Create a session
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (compatible; LearningScraper/1.0)"
})

# Step 4: Scrape all pages
while url:
    try:
        print("Scraping:", url)

        response = session.get(url, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Find all books on this page
        books = soup.find_all("article", class_="product_pod")

        if not books:
            print("No books found. Stopping.")
            break

        # Step 5: Extract book details
        for book in books:
            title = book.find("h3").find("a")["title"].strip()

            price = book.find(
                "p", class_="price_color"
            ).get_text(strip=True)

            rating_classes = book.find(
                "p", class_="star-rating"
            )["class"]
            rating = rating_classes[1]

            availability = book.find(
                "p", class_="availability"
            ).get_text(" ", strip=True)

            # Remove duplicate titles
            if title not in seen_titles:
                seen_titles.add(title)

                data.append({
                    "Title": title,
                    "Price": price,
                    "Rating": rating,
                    "Availability": availability
                })

        # Step 6: Find the next page
        next_page = soup.find("li", class_="next")

        if next_page:
            next_link = next_page.find("a")["href"]
            url = urljoin(url, next_link)
            time.sleep(1)
        else:
            url = None

    except requests.RequestException as error:
        print("Request failed:", error)
        break

# Step 7: Save data to CSV
if data:
    with open(
        "books.csv",
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:
        fieldnames = [
            "Title", "Price", "Rating", "Availability"
        ]

        writer = csv.DictWriter(
            file, fieldnames=fieldnames
        )
        writer.writeheader()
        writer.writerows(data)

    print("\nScraping completed!")
    print("Total unique books scraped:", len(data))
    print("Data saved to books.csv")
else:
    print("No data collected. CSV was not created.")
