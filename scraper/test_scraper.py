from scraper.browser import get_driver
from scraper.twitter_scraper import scrape_tweets

driver = get_driver()
tweets = scrape_tweets(driver)
driver.quit()

print(f"Collected tweets: {len(tweets)}")
print(tweets[0])
