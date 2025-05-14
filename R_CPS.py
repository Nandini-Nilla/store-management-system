from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle
# import oracle_connect
import cx_Oracle as cs
from PIL import ImageTk, Image


def products():
    con = cs.connect('name/password@localhost')
    cur = con.cursor()
    con.commit()

    window = tk.Tk()
    window.title('Product Details')
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry("%dx%d" % (width, height))

    cur.execute("SELECT * FROM product_table")

    e=Label(window,width=20,text='Product Number',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(window,width=20,text='Product Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(window,width=20,text='Product Description',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(window,width=20,text='Product Price',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=Label(window,width=20,text='Category Number',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    e=Label(window,width=20,text='Expiry Date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=5)
    e = Label(window, width=20, text='Quantity', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=6)

    i = 1

    for s in cur:
        for j in range(len(s)):
            e = Label(window, width=10, text=s[j],
                      borderwidth=0, relief='ridge', anchor="w")

            e = Entry(window, width=23, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, s[j])
        i = i + 1


def category():
    con = cs.connect('name/password@localhost')
    cur = con.cursor()
    con.commit()

    window = tk.Tk()
    window.title('Category Details')
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry("%dx%d" % (width, height))

    cur.execute("SELECT * FROM category_table")

    e=Label(window,width=20,text='Category Number',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(window,width=20,text='Category Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(window,width=20,text='Category Description',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)

    i=1

    for s in cur:
        for j in range(len(s)):
            e = Label(window, width=10, text=s[j],
                      borderwidth=0, relief='ridge', anchor="w")

            e = Entry(window, width=23, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, s[j])
        i=i+1

def supplier():
    con = cs.connect('name/password@localhost')
    cur = con.cursor()
    con.commit()

    window = tk.Tk()
    window.title('Supplier Details')
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry("%dx%d" % (width, height))

    cur.execute("SELECT * FROM supplier_table")

    e=Label(window,width=20,text='Supplier Number',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(window,width=20,text='Supplier Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(window,width=20,text='Supplier Company',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(window,width=20,text='Supplier Location',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=Label(window,width=20,text='Phone Number',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)

    i=1

    for s in cur:
        for j in range(len(s)):
            e = Label(window, width=10, text=s[j],
                      borderwidth=0, relief='ridge', anchor="w")

            e = Entry(window, width=23, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, s[j])
        i=i+1

def employee():
    con = cs.connect('name/password@localhost')
    cur = con.cursor()
    con.commit()

    window = tk.Tk()
    window.title('Employee Details')
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry("%dx%d" % (width, height))

    cur.execute("SELECT * FROM employee_table")

    e=Label(window,width=20,text='Employee Number',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(window,width=20,text='Employee Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(window,width=20,text='Employee Phone Number',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)

    i=1

    for s in cur:
        for j in range(len(s)):
            e = Label(window, width=10, text=s[j],
                      borderwidth=0, relief='ridge', anchor="w")

            e = Entry(window, width=23, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, s[j])
        i=i+1