
"""
Created on Fri Sep 11 13:25:14 2020

@author: Igor
"""

from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("400x600")
root.title("Stocks Register")       

Title = Label(root, text="Purchase and Sale Register",anchor=CENTER)
Title["font"] = ("Arial", "10", "bold")
Title.place(height=25, relx=0.3, rely=0.04)
Title.pack()


Ticker_label = Label(root, text="TICKER:")
Ticker_label["font"] = ("Arial", "10", "bold")
Ticker_label.place(height=25, relx=0.01, rely=0.08)
 
Ticker_entry = Entry(root)
Ticker_entry["font"] = ("Arial", "10")
Ticker_entry.place(height=20, relx=0.16, rely=0.08, width=184)

  

QTY_label = Label(root, text="QTY:")
QTY_label["font"] = ("Arial", "10")
QTY_label.place(height=20, relx=0.01, rely=0.14)
  
QTY_entry = Entry(root)
QTY_entry["font"] = ("Arial", "10")
QTY_entry.place(height=20, relx=0.16,rely=0.14,width=60)

Unitary_price_label = Label(root, text="UN Price:")
Unitary_price_label["font"] = ("Arial", "10")
Unitary_price_label.place(height=20, relx=0.28, rely=0.14)

Unitary_price_entry = Entry(root)
Unitary_price_entry["font"] = ("Arial", "10")
Unitary_price_entry.place(height=20, relx=0.44,rely=0.14,width=70)

Date_label = Label(root, text="Date:")
Date_label["font"] = ("Arial", "10")
Date_label.place(height=20, relx=0.01, rely=0.195)

Date_entry = Entry(root)
Date_entry["font"] = ("Arial", "10")
Date_entry.place(height=20, relx=0.16,rely=0.195,width=100)

Class_label = Label(root, text="Class/Market:")
Class_label["font"] = ("Arial", "10")
Class_label.place(height=20, rely=0.25, relx=0.3)

Class_box = ttk.Combobox(root, values=["Select Class:", "Stocks", "FII","ETF","REITS"])       
Class_box.place(height=20, relx=0.14,rely=0.28,width=92)
Class_box.current(0)

Class_box = ttk.Combobox(root, values=["Select Market:", "B3", "US","EU"])       
Class_box.place(height=20, relx=0.4,rely=0.28,width=94)
Class_box.current(0)


Purchase_button = Button(root, text="Purchase Register", command=False)
Purchase_button.place(height=25, relx=0.08,rely=0.35,width=110)

Sale_button = Button(root, text="Sale Register", command=False)
Sale_button.place(height=25, relx=0.38,rely=0.35,width=110)

root.mainloop()