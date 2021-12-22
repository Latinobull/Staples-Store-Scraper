from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from soup import Soupify
from createFile import showFile
from selenium.common.exceptions import NoSuchElementException


def Start(numbers):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    storeList = []
    try:
        for store in numbers:

            PAGE = f"https://stores.staples.com/search?storeId={store}&qp={store}&l=en"

            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--incognito')
            options.add_argument('--headless')
            driver = webdriver.Chrome(PATH, chrome_options=options)
            driver.get(PAGE)
            driver.find_element(By.CLASS_NAME, 'Teaser-titleLink').click()
            source = driver.page_source
            driver.quit()
            Soupify(source, storeList)
    except NoSuchElementException:
        print(f'Store {store} doesnt exist')
        driver.quit()
        return
    showFile()
