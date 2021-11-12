from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from bs4 import BeautifulSoup


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
    time.sleep(1)
    storeNum = driver.find_element(By.CLASS_NAME, 'Core-storeId').text
    street = driver.find_element(By.CLASS_NAME, 'c-address-street-1').text
    city = driver.find_element(By.CLASS_NAME, 'c-address-city').text
    state = driver.find_element(By.CLASS_NAME, 'c-address-state').text
    zipcode = driver.find_element(
        By.CLASS_NAME, 'c-address-postal-code').text
    phone = str(driver.find_element(By.ID, 'phone-main').text)
    print(
        f'{storeNum} is located at {street} {city}, {state} {zipcode}. The phone number is {phone}')
    source = driver.page_source
    driver.quit()


Start(1232)
