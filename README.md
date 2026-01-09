# Real-Time Market Intelligence System – Indian Stock Market

## Overview
This project implements a **real-time data collection and analysis system** for Indian stock market intelligence using Twitter/X discussions.  
The system scrapes live market-related tweets, processes and cleans textual data, converts it into quantitative signals, and generates aggregated trading insights.

⚠️ **No paid APIs or Twitter API are used.**  
All data collection is performed using Selenium in a compliant, real-world manner.

---

## Key Objectives
- Collect real-time Indian stock market discussions from Twitter/X
- Process and normalize multilingual (Indian language) text data
- Convert unstructured text into quantitative trading signals
- Design a scalable, memory-efficient, production-ready pipeline

---

## Features
- Selenium-based Twitter/X scraping (no API usage)
- Persistent login session handling
- Hashtag tracking: #nifty50, #sensex, #intraday, #banknifty
- Unicode-safe text cleaning (supports Hindi, Marathi, Hinglish, emojis)
- Hash-based deduplication (O(1) lookup)
- Parquet-based columnar storage
- TF-IDF text-to-signal conversion
- Composite trading signal with confidence intervals
- Memory-efficient visualization using sampling
- Modular, scalable architecture

---

## Tech Stack
- Python 3.10+
- Selenium
- Pandas, NumPy
- PyArrow (Parquet)
- Scikit-learn
- Matplotlib

---

## Project Structure
market-intelligence/
├── scraper/
├── processing/
├── storage/
├── analysis/
├── utils/
├── data/
│   ├── raw/
│   └── processed/
├── requirements.txt
├── README.md
└── TECHNICAL_DOC.md

---

## Installation
pip install -r requirements.txt

---

## Twitter/X Login (One-Time)
Run:
python scraper/test_browser.py

Login manually once. Session is reused automatically.

---

## Running the Pipeline
1. Scrape tweets:
python storage/test_parquet.py

2. Process data:
python processing/process_pipeline.py

3. Generate signals:
python analysis/test_aggregation.py

4. Visualize:
python analysis/test_visualize.py

---

## Disclaimer
For educational and analytical purposes only. Not financial advice.
