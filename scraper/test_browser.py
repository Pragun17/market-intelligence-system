from scraper.browser import get_driver
import time

driver = get_driver()
driver.get("https://twitter.com")
time.sleep(10)
driver.quit()
