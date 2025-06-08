import tkinter
from tkinter import ttk
import csv

def load_data(treeview):
    try:
        with open('game_scores.csv', 'r') as file:
            reader = csv.reader(file)
            #Making first row the headers
            headers = next(reader)
            # Inserting headers into the treeview
            treeview['columns'] = headers
            treeview.heading('#0', text='Index')  # Index column
            for header in headers:
                treeview.heading(header, text=header)
            # Inserting data into the treeview
            for i, row in enumerate(reader, 1):
                treeview.insert('', 'end', text=str(i), values=row)
    except Exception as e:
        print("Error:", e)

window2 = tkinter.Tk()
window2.title("CSV Data Table")
window2.geometry("600x420")

# Creating a Treeview widget
treeview = ttk.Treeview(window2, show='headings')
treeview.pack(fill='both', expand=True)

# Load data from CSV file
load_data(treeview)

window2.mainloop()