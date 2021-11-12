from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from soup import Soupify


def Start(storeNumber):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    PAGE = f"https://stores.staples.com/search?storeId={storeNumber}&qp={storeNumber}&l=en"

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(PATH, chrome_options=options)
    driver.get(PAGE)

    text = driver.find_element(By.CLASS_NAME, 'Teaser-titleLink').text
    print(text)
    driver.find_element(By.CLASS_NAME, 'Teaser-titleLink').click()
    source = driver.page_source
    driver.quit()
    Soupify(source)


Start(1232)
