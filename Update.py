from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle
#import oracle_connect
import cx_Oracle as cs
from PIL import ImageTk, Image

import U_PCS
import Crud_Op

def update_func():


    window_update = tk.Tk()
    window_update.title('UPDATE PAGE')
    #window_create.geometry("800x200+288+78")

    width = window_update.winfo_screenwidth()
    height = window_update.winfo_screenheight()
    window_update.geometry("%dx%d" % (width, height))

    tk.image_home = ImageTk.PhotoImage(file="insertion.jpg")
    tk.label = tk.Label(window_update, image=tk.image_home)
    tk.label.pack()

    def call_crud():
        window_update.destroy()
        Crud_Op.crud_func()

    menubar = Menu(window_update)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Menu", command=call_crud)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=window_update.destroy)
    menubar.add_cascade(label="FILE", menu=filemenu)

    window_update.config(menu=menubar)

    def enter_product_table():
        is_ok = tk.messagebox.askyesno('welcome', 'Do you want to update ??? ')
        #print(is_ok)
        if is_ok:
            window_update.destroy()
            U_PCS.update_product_func()


    def enter_category_table():
        is_ok = tk.messagebox.askyesno('welcome', 'Do you want to update ??? ')
        if is_ok:
            window_update.destroy()
            U_PCS.update_category_func()

    def enter_supplier_table():
        is_ok = tk.messagebox.askyesno('welcome', 'Do you want to update ??? ')
        if is_ok:
            window_update.destroy()
            U_PCS.update_supplier_func()



    bt_insert = tk.Label(window_update, text='UPDATION', fg='black',font=("Arial", 20))
    bt_insert.place(x=650, y=220, width=200)


    bt_product = tk.Button(window_update, text='PRODUCT', activebackground="gray", activeforeground='white',
                          fg='black', bg="#F0F8FF", font=("Arial", 15), command=enter_product_table)
    bt_product.place(x=250, y=400, width=200)

    bt_supplier = tk.Button(window_update, text='SUPPLIER', activebackground="gray", activeforeground='white',
                          fg='black', bg="#F0F8FF", font=("Arial", 15), command=enter_supplier_table)
    bt_supplier.place(x=650, y=400, width=200)

    bt_category = tk.Button(window_update, text='CATEGORY', activebackground="gray", activeforeground='white',
                          fg='black', bg="#F0F8FF", font=("Arial", 15), command=enter_category_table)
    bt_category.place(x=1050, y=400, width=200)



    window_update.mainloop()

#update_func()