from tkinter import *
from tkinter import ttk
from back import Start


def runThis():
    numbers = storeNumberValue.get()
    newNumber = numbers.lower()
    if newNumber.islower():
        print('Nnumbers only please')
        return
    numbers = numbers.split(sep=',')

    Start(numbers)


root = Tk()
root.title('Staples Scraper')
frm = ttk.Frame(root, padding=5, width=550, height=150)
frm.grid()
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)

store_label = ttk.Label(root, text='Enter Store Numbers', font='none 30 bold')
store_label.config(anchor=CENTER)
store_label.grid(column=0, row=0, sticky='NSEW')

subTitle = ttk.Label(
    root, text='Seperate each store with a comma for best results', font='none 20 normal ')
subTitle.config(anchor=CENTER)
subTitle.grid(column=0, row=1, sticky='NSEW')

global storeNumberValue
storeNumberValue = StringVar()
store_entry = ttk.Entry(root, textvariable=storeNumberValue)
store_entry.grid(column=0, row=2, sticky='NSEW')

searchButton = ttk.Button(root, command=runThis, text='Submit')
searchButton.grid(column=0, row=3, sticky='NSEW')

root.mainloop()
