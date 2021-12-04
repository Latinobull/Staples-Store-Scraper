from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Staples Scraper')
frm = ttk.Frame(root, padding=10, width=50, height=50)
frm.grid()
store_label = ttk.Label(root, text='Enter Stores')
store_label.grid(column=0, row=0)
store_entry = ttk.Entry(root, )
store_entry.grid(column=0, row=1)

root.mainloop()
