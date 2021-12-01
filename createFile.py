import csv


def createFile(storeList):
    storeColumns = ['Store#', 'Street', 'City', 'State', 'Zipcode']
    with open('store.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=storeColumns)
        writer.writeheader()
        for data in storeList:
            writer.writerow(data)
