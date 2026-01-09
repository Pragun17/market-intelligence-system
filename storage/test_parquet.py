from scraper.browser import get_driver
from scraper.twitter_scraper import scrape_tweets
from storage.parquet_store import save_parquet
from utils.config import RAW_DATA_PATH

driver = get_driver()
tweets = scrape_tweets(driver)
driver.quit()

save_parquet(tweets, RAW_DATA_PATH)
