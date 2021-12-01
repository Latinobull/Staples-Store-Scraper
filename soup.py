from bs4 import BeautifulSoup


def Soupify(source, storeList):
    soup = BeautifulSoup(source, 'html.parser')
    all = soup.find_all('div', {'class': 'Main-core'})
    # print(all)

    d = {}
    d['Store#'] = soup.find('div', {'class': 'Core-storeId'}).text
    for item in all:
        d['Street'] = item.find(
            'span', {'class': 'c-address-street-1'}).text
        d['City'] = item.find('span', {'class': 'c-address-city'}).text
        d['State'] = item.find('abbr', {'class': 'c-address-state'}).text
        d['Zipcode'] = item.find(
            'span', {'class': 'c-address-postal-code'}).text
    storeList.append(d)
    print(storeList)
