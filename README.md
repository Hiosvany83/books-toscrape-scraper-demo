# Demo Web Scraper — books.toscrape.com

**Sample / demonstration project** (not client work). Built to show
Python web-scraping, data cleaning and CSV export skills.

## What it does

Scrapes the first 3 catalogue pages of [books.toscrape.com](https://books.toscrape.com)
(a public demo site made specifically for practising scraping) and extracts
for each book: **title, price, star rating, availability**. Output is saved
as a clean UTF-8 CSV.

## Install & run (under 2 minutes)

```
pip install -r requirements.txt
python scraper_demo.py
```

Expected output:

```
page 1: 20 books so far
page 2: 40 books so far
page 3: 60 books so far
saved 60 books -> books_sample.csv
```

## Sample output (`books_sample.csv`, first rows)

```
title,price,rating,availability
A Light in the Attic,£51.77,3,In stock
Tipping the Velvet,£53.74,1,In stock
Soumission,£50.10,1,In stock
```

## Notes

* Respects the target site: demo domain, small page count, no login, no JS rendering needed.
* Cleaning applied: whitespace stripped from all fields; star rating mapped from the CSS class to an integer 1–5; response encoding forced to UTF-8 so prices and apostrophes are not corrupted.
