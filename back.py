from selenium import webdriver
import time
# from bs4 import BeautifulSoup


def Start(storeNumber):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    PAGE = f"https://stores.staples.com/search?storeId={storeNumber}&qp={storeNumber}&l=en"
    driver = webdriver.Chrome(PATH)
    driver.get(PAGE)

    while True:
        text = driver.find_element_by_class_name('Teaser-titleLink').text
        print(text)
        driver.find_element_by_class_name('Teaser-titleLink').click()

        time.sleep(20)
        break


Start(1232)
