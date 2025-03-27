from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def scrapeList(link):
    """Scrapes and returns a list of all titles from an IMDb list.
    LINK (string): Link of IMDb list"""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.imdb.com/user/ur159205241/ratings/")

    try:
        cookie_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='accept-button']"))
        )
        cookie_btn.click()
    except:
        pass

    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    items = soup.find_all("li", class_="ipc-metadata-list-summary-item")

    title_list = []

    for item in items:
        title_wrapper = item.find("h3", class_="ipc-title__text")
        title = title_wrapper.get_text(strip=True) if title_wrapper else "N/A"
        
        title_list.append(title.split('. ', 1)[-1])

    return title_list
