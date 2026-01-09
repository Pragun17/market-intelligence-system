import time
import random
import re
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from utils.config import HASHTAGS, TWEET_TARGET
from utils.logger import setup_logger

logger = setup_logger()


def extract_metrics(tweet):
    try:
        metrics = tweet.find_elements(By.XPATH, ".//span")
        return {
            "likes": metrics[-1].text if len(metrics) >= 1 else 0,
            "retweets": metrics[-2].text if len(metrics) >= 2 else 0,
            "replies": metrics[-3].text if len(metrics) >= 3 else 0,
        }
    except Exception:
        return {"likes": 0, "retweets": 0, "replies": 0}


def extract_tweet(tweet):
    text = tweet.text
    hashtags = re.findall(r"#\w+", text)
    mentions = re.findall(r"@\w+", text)

    return {
        "username": "unknown",  # Twitter hides this without login
        "timestamp": datetime.utcnow(),
        "content": text,
        "hashtags": hashtags,
        "mentions": mentions,
        **extract_metrics(tweet)
    }


def scrape_tweets(driver):
    tweets_data = []
    cutoff_time = datetime.utcnow() - timedelta(hours=24)

    for tag in HASHTAGS:
        logger.info(f"Scraping #{tag}")
        driver.get(f"https://twitter.com/search?q=%23{tag}&f=live")
        time.sleep(random.uniform(4, 6))

        while len(tweets_data) < TWEET_TARGET:
            tweets = driver.find_elements(By.XPATH, "//article")

            for tweet in tweets:
                data = extract_tweet(tweet)
                if data["timestamp"] < cutoff_time:
                    return tweets_data
                tweets_data.append(data)

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.uniform(2, 4))

            logger.info(f"Collected {len(tweets_data)} tweets")

    return tweets_data
