from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle
#import oracle_connect
import cx_Oracle as cs
from PIL import ImageTk, Image

import C_PCS

def create_func():

    window_create = tk.Tk()
    window_create.title('CREATE PAGE')
    #window_create.geometry("800x200+288+78")

    width = window_create.winfo_screenwidth()
    height = window_create.winfo_screenheight()
    window_create.geometry("%dx%d" % (width, height))


    tk.image_home = ImageTk.PhotoImage(file="insertion.jpg")
    tk.label = tk.Label(window_create, image=tk.image_home)
    tk.label.pack()


    def enter_product_table():
        is_ok = tk.messagebox.askyesno('welcome', 'Do you want to insert ??? ')
        #print(is_ok)
        if is_ok:
            window_create.destroy()
            C_PCS.product_func()


    def enter_category_table():
        is_ok = tk.messagebox.askyesno('welcome', 'Do you want to insert ??? ')
        if is_ok:
            window_create.destroy()
            C_PCS.category_func()

    def enter_supplier_table():
        is_ok = tk.messagebox.askyesno('welcome', 'Do you want to insert ??? ')
        if is_ok:
            window_create.destroy()
            C_PCS.supplier_func()

    def call_crud():
        window_create.destroy()
        import Crud_Op
        Crud_Op.crud_func()

    menubar = Menu(window_create)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Menu", command=call_crud)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=window_create.destroy)
    menubar.add_cascade(label="FILE", menu=filemenu)

    window_create.config(menu=menubar)


    '''

    def enter_product_table():
        import Product
        Product.product_func()

    def enter_supplier_table():
        import Supplier
        Supplier.supplier_func()

    def enter_category_table():
        import Category
        Category.category_func()

    '''


    bt_insert = tk.Label(window_create, text='INSERTION', fg='black',font=("Arial", 20))
    bt_insert.place(x=650, y=220, width=200)


    bt_product = tk.Button(window_create, text='PRODUCT', activebackground="gray", activeforeground='white',
                          fg='black', bg="#F0F8FF", font=("Arial", 15), command=enter_product_table)
    bt_product.place(x=250, y=400, width=200)

    bt_supplier = tk.Button(window_create, text='SUPPLIER', activebackground="gray", activeforeground='white',
                          fg='black', bg="#F0F8FF", font=("Arial", 15), command=enter_supplier_table)
    bt_supplier.place(x=650, y=400, width=200)

    bt_category = tk.Button(window_create, text='CATEGORY', activebackground="gray", activeforeground='white',
                          fg='black', bg="#F0F8FF", font=("Arial", 15), command=enter_category_table)
    bt_category.place(x=1050, y=400, width=200)



    window_create.mainloop()

#create_func()