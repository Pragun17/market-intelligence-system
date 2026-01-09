# Technical Documentation – Market Intelligence System

## 1. Project Overview
This project implements a **real-time market intelligence system** using Twitter/X data for Indian stock market analysis.  
It collects tweets, cleans and deduplicates text, converts textual content into numerical signals, and aggregates them into a **composite trading signal**.

**No paid APIs or Twitter API are used.**

---

## 2. Data Collection
- **Method:** Selenium browser automation
- **Target:** Tweets containing hashtags `#nifty50`, `#sensex`, `#intraday`, `#banknifty`
- **Data extracted:**
  - Username
  - Timestamp
  - Content
  - Engagement metrics
  - Mentions
  - Hashtags
- **Rate-limiting & anti-bot handling:**
  - Randomized delays
  - Human-like scrolling
  - Persistent login session

---

## 3. Data Processing
1. **Cleaning & Normalization**
   - Unicode-safe regex to preserve Indian languages & emojis
   - URL removal, whitespace normalization, lowercase conversion
   - Removal of very short tweets
2. **Deduplication**
   - Hash-based deduplication using MD5 of normalized text
   - O(1) lookup efficiency for large datasets

---

## 4. Data Storage
- **Format:** Apache Parquet (columnar storage)
- **Structure:**
  - `data/raw` → raw tweets
  - `data/processed` → cleaned & deduplicated tweets
- Efficient for analytics and low memory usage

---

## 5. Text-to-Signal Conversion
- TF-IDF vectorization
  - Unigrams & bigrams
  - Feature limit for memory efficiency
- Captures market-specific terms (e.g., `banknifty breakout`, `nifty bullish`)

---

## 6. Signal Aggregation
- Domain-specific keywords assigned weights:
  - Bullish: +1 (`bullish`, `buy`, `rally`, `breakout`)
  - Bearish: -1 (`bearish`, `sell`, `crash`, `breakdown`)
- TF-IDF weighted sum generates **raw signal per tweet**
- Aggregated statistics:
  - Mean
  - Standard deviation
  - Confidence interval

---

## 7. Visualization
- **Memory-efficient histogram** of signal distribution
- Random sampling if dataset is large
- Single lightweight Matplotlib plot

---

## 8. Scalability & Performance
- Modular pipeline allows 10× data scaling
- Hash-based deduplication for O(1) efficiency
- Columnar Parquet storage reduces memory footprint
- Sampling-based visualization prevents memory spikes

---

## 9. Conclusion
The system demonstrates:
- Real-world problem solving under constraints
- Efficient data processing & storage
- Explainable signal generation for algorithmic trading
- Production-level software engineering practices
