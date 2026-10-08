# Demo Web Scraper — books.toscrape.com

**Sample / demonstration project** (not client work). Built to show
Python web-scraping, data cleaning and CSV export skills.

## What it does
Scrapes the first 3 catalogue pages of [books.toscrape.com](https://books.toscrape.com)
(a public demo site made specifically for practising scraping) and extracts
for each book: **title, price, star rating, availability**. Output is saved
as a clean UTF-8 CSV.

## Install & run (under 2 minutes)
```bash
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
```csv
title,price,rating,availability
A Light in the Attic,£51.77,Three,In stock
Tipping the Point Scale,£53.74,One,In stock
Soumission,£50.10,One,In stock
```

## Notes
- Respects the target site: demo domain, small page count, no login, no JS rendering needed.
- Cleaning applied: whitespace stripped from all fields, rating normalised from CSS class to word.
