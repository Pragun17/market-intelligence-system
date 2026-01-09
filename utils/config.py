from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

HASHTAGS = ["nifty50", "sensex", "intraday", "banknifty"]
TWEET_TARGET = 300  # dev value

RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "tweets.parquet"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "clean_tweets.parquet"
