"""
Demo web scraper — books.toscrape.com
=====================================

Sample/demonstration project (not client work).

Extracts book title, price, rating and availability from the first
N catalogue pages of books.toscrape.com (a public demo site built
specifically for practising web scraping) and saves the result to CSV.

Usage:
    pip install -r requirements.txt
    python scraper_demo.py          # scrapes 3 pages -> books_sample.csv
"""

import csv

import requests
from bs4 import BeautifulSoup

BASE = "https://books.toscrape.com/catalogue/page-{}.html"
PAGES = 3
OUTPUT = "books_sample.csv"

RATINGS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def parse_page(url):
    """Fetch one catalogue page and return a list of book dicts."""
    resp = requests.get(url, timeout=20)
    resp.raise_for_status()
    # books.toscrape.com serves UTF-8 but does not always declare it in the
    # headers; without this, requests falls back to ISO-8859-1 and the CSV
    # ends up with mojibake (e.g. "Â£51.77" instead of "£51.77").
    resp.encoding = "utf-8"
    soup = BeautifulSoup(resp.text, "html.parser")

    books = []
    for article in soup.select("article.product_pod"):
        title = article.h3.a["title"].strip()
        price = article.select_one("p.price_color").get_text(strip=True)
        rating_word = article.select_one("p.star-rating")["class"][1]
        rating = RATINGS.get(rating_word, rating_word)
        availability = article.select_one("p.instock.availability").get_text(strip=True)
        books.append(
            {
                "title": title,
                "price": price,
                "rating": rating,
                "availability": availability,
            }
        )
    return books


def main():
    all_books = []
    for page in range(1, PAGES + 1):
        all_books.extend(parse_page(BASE.format(page)))
        print(f"page {page}: {len(all_books)} books so far")

    with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["title", "price", "rating", "availability"]
        )
        writer.writeheader()
        writer.writerows(all_books)

    print(f"saved {len(all_books)} books -> {OUTPUT}")


if __name__ == "__main__":
    main()
