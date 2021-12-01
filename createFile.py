import csv
import os


def createFile(storeList):
    storeColumns = ['Store#', 'Street', 'City', 'State', 'Zipcode']
    with open('store.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=storeColumns)
        writer.writeheader()
        for data in storeList:
            if any(field.strip() for field in data):
                writer.writerow(data)


def testingCircular():
    os.system(r'store.csv')
