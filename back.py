from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from soup import Soupify
from createFile import testingCircular


def Start(*args):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    storeList = []
    for store in args:

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
    testingCircular()


Start('0001', 1257, 1231, 1795, 1232)
