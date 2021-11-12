from bs4 import BeautifulSoup


def Soupify(source):
    soup = BeautifulSoup(source, 'html.parser')
    all = soup.find_all('div', {'class': 'Main-core'})
    # print(all)

    l = []
    d = {}
    d['Store#'] = soup.find('div', {'class': 'Core-storeId'}).text
    for item in all:
        d['Street'] = item.find(
            'span', {'class': 'c-address-street-1'}).text
    l.append(d)
    print(l)
