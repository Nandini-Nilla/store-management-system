from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle
# import oracle_connect
import cx_Oracle as cs
from PIL import ImageTk, Image
import Create
import login


def product_func():
    con = cs.connect('nandini/123456@localhost')
    cur = con.cursor()

    window_product = tk.Tk()
    # window_product.geometry('500x400+500+250')
    window_product.title('Products')
    width = window_product.winfo_screenwidth()
    height = window_product.winfo_screenheight()
    window_product.geometry("%dx%d" % (width, height))

    window_product.configure(bg='white')

    tk.image_home = ImageTk.PhotoImage(file="cart_image.jpg")
    tk.label = tk.Label(window_product, image=tk.image_home)
    tk.label.place(x=0, y=0)

    def call_crud():
        window_product.destroy()
        Create.create_func()

    def call_login():
        window_product.destroy()
        login.login_func()

    menubar = Menu(window_product)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Back", command=call_crud)

    filemenu.add_separator()

    filemenu.add_command(label="Logout", command=call_login)
    menubar.add_cascade(label="Menu", menu=filemenu)

    window_product.config(menu=menubar)

    ########insertion into database##################
    def sign_to_oracle():
        new_p_id = prod_id.get()
        new_p_name = prod_name.get()
        new_p_desc = prod_desc.get()
        new_p_price = prod_price.get()
        new_c_id = category_id.get()
        new_p_e_d = prod_expiry_id.get()
        new_p_quan = prod_quantity_id.get()

        sql_insert_product_t = "insert into product_table(prod_id,prod_name,prod_desc,prod_price,category_id,prod_expiry_date,quantity) values('{}','{}','{}','{}','{}','{}','{}')".format(
            new_p_id, new_p_name, new_p_desc, new_p_price, new_c_id, new_p_e_d, new_p_quan)

        cur.execute("select prod_id from product_table where prod_id = '{}'".format(new_p_id))
        row = cur.fetchall()

        if (row == []):
            if (
                    new_p_id == '' or new_p_name == '' or new_p_desc == '' or new_p_price == '' or new_c_id == '' or new_p_e_d == '' or new_p_quan == ''):
                tk.messagebox.showerror('error', 'All fields are required')
            else:
                cur.execute(sql_insert_product_t)
                con.commit()
                tk.messagebox.showinfo('welcome', 'Product Inserted!!!')

            # product_id and label, inputbox

    tk.Label(window_product, text='PRODUCT DATA', font=('Georgia', 20), bg='white').place(x=600, y=30)

    prod_id = tk.StringVar()
    tk.Label(window_product, text='Product Number:', font='Algerian', bg='white').place(x=550, y=90)
    tk.Entry(window_product, textvariable=prod_id, bd=3, ).place(x=750, y=95)

    # product_name and label, input box
    prod_name = tk.StringVar()
    tk.Label(window_product, text='Product Name:', font='Algerian', bg='white').place(x=550, y=180)
    tk.Entry(window_product, textvariable=prod_name, bd=3).place(x=750, y=185)

    # product_description and label, input box
    prod_desc = tk.StringVar()
    tk.Label(window_product, text='Product Description:', font='Algerian', bg='white').place(x=550, y=270)
    tk.Entry(window_product, textvariable=prod_desc, bd=3).place(x=750, y=275)

    # Product_price variable and label, input box
    prod_price = tk.StringVar()
    tk.Label(window_product, text='Product Price:', font='Algerian', bg='white').place(x=550, y=360)
    tk.Entry(window_product, textvariable=prod_price, bd=3).place(x=750, y=365)

    category_id = tk.StringVar()
    tk.Label(window_product, text='Category Number:', font='Algerian', bg='white').place(x=550, y=450)
    tk.Entry(window_product, textvariable=category_id, bd=3).place(x=750, y=455)

    prod_quantity_id = tk.StringVar()
    tk.Label(window_product, text='Product Quantity:', font='Algerian', bg='white').place(x=550, y=540)
    tk.Entry(window_product, textvariable=prod_quantity_id, bd=3).place(x=750, y=545)

    # Product_Expiry_date variables and labels, input boxes
    prod_expiry_id = tk.StringVar()
    tk.Label(window_product, text='Product Expiry Date:', font='Algerian', bg='white').place(x=550, y=630)
    tk.Entry(window_product, textvariable=prod_expiry_id, bd=3).place(x=750, y=635)

    bt_submit = tk.Button(window_product, text='Submit', font='Algerian', bg='white', command=sign_to_oracle)
    bt_submit.place(x=630, y=690, width=200)

    window_product.mainloop()


# product_func()

def category_func():
    con = cs.connect('nandini/123456@localhost')
    cur = con.cursor()

    window_category = tk.Tk()
    # window_product.geometry('500x400+500+250')
    window_category.title('Category')
    width = window_category.winfo_screenwidth()
    height = window_category.winfo_screenheight()
    window_category.geometry("%dx%d" % (width, height))

    tk.image_home = ImageTk.PhotoImage(file="cart_image.jpg")
    tk.label = tk.Label(window_category, image=tk.image_home)
    tk.label.pack()

    def call_crud():
        window_category.destroy()
        Create.create_func()

    def call_login():
        window_category.destroy()
        login.login_func()

    menubar = Menu(window_category)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Back", command=call_crud)

    filemenu.add_separator()

    filemenu.add_command(label="Logout", command=call_login)
    menubar.add_cascade(label="Menu", menu=filemenu)

    window_category.config(menu=menubar)

    ########insertion into database##################
    def sign_to_oracle():
        new_c_id = category_id.get()
        new_c_name = category_name.get()
        new_c_desc = category_desc.get()

        sql_insert_category_t = "insert into category_table(category_id,category_name,category_desc) values('{}','{}','{}')".format(
            new_c_id, new_c_name, new_c_desc)

        cur.execute("select category_id from category_table where category_id = '{}'".format(new_c_id))
        row = cur.fetchall()

        if (row == []):
            if (new_c_id == '' or new_c_name == '' or new_c_desc == ''):
                tk.messagebox.showerror('error', 'All fields are required')
            else:
                cur.execute(sql_insert_category_t)
                con.commit()
                tk.messagebox.showinfo('welcome', 'Category Inserted!!!')

    tk.Label(window_category, text='CATEGORY DATA', font=('Georgia', 20), bg='white').place(x=610, y=130)

    # category_id and label, inputbox
    category_id = tk.StringVar()
    tk.Label(window_category, text='Category Number:', font='Algerian', bg='white').place(x=550, y=250)
    tk.Entry(window_category, textvariable=category_id, bd=3).place(x=750, y=255)

    # category_name and label, input box
    category_name = tk.StringVar()
    tk.Label(window_category, text='Category Name:', font='Algerian', bg='white').place(x=550, y=350)
    tk.Entry(window_category, textvariable=category_name, bd=3).place(x=750, y=355)

    # category_description and label, input box
    category_desc = tk.StringVar()
    tk.Label(window_category, text='Category Description:', font='Algerian', bg='white').place(x=550, y=450)
    tk.Entry(window_category, textvariable=category_desc, bd=3).place(x=750, y=455)

    # Product_price variable and label, input box

    bt_submit = tk.Button(window_category, text='Submit', font='Algerian', bg='white', command=sign_to_oracle)
    bt_submit.place(x=630, y=550, width=200)

    window_category.mainloop()


# category_func()

def supplier_func():
    con = cs.connect('nandini/123456@localhost')
    cur = con.cursor()

    window_supplier = tk.Tk()
    # window_product.geometry('500x400+500+250')
    window_supplier.title('Supplier Info')
    width = window_supplier.winfo_screenwidth()
    height = window_supplier.winfo_screenheight()
    window_supplier.geometry("%dx%d" % (width, height))

    tk.image_home = ImageTk.PhotoImage(file="cart_image.jpg")
    tk.label = tk.Label(window_supplier, image=tk.image_home)
    tk.label.pack()

    def call_crud():
        window_supplier.destroy()
        Create.create_func()

    def call_login():
        window_supplier.destroy()
        login.login_func()

    menubar = Menu(window_supplier)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Back", command=call_crud)

    filemenu.add_separator()

    filemenu.add_command(label="Logout", command=call_login)
    menubar.add_cascade(label="Menu", menu=filemenu)

    window_supplier.config(menu=menubar)

    ########insertion into database##################
    def sign_to_oracle():
        new_s_id = supl_id.get()
        new_s_name = supl_name.get()
        new_s_com = supl_company.get()
        new_s_loc = supl_loc.get()
        new_s_p_num = supl_phone_num.get()

        sql_insert_supplier_t = "insert into supplier_table(supl_id,supl_name,supl_company,supl_loc,phone_number) values('{}','{}','{}','{}','{}')".format(
            new_s_id, new_s_name, new_s_com, new_s_loc, new_s_p_num)

        cur.execute("select supl_id from supplier_table where supl_id = '{}'".format(new_s_id))
        row = cur.fetchall()

        if (row == []):
            if (new_s_id == '' or new_s_name == '' or new_s_com == '' or new_s_loc == '' or new_s_p_num == ''):
                tk.messagebox.showerror('error', 'All fields are required')
            else:
                cur.execute(sql_insert_supplier_t)
                con.commit()
                tk.messagebox.showinfo('welcome', 'Supplier Inserted!!!')

    tk.Label(window_supplier, text='SUPPLIER DATA', font=('Georgia', 20), bg='white').place(x=610, y=50)
    # supplier_id and label, inputbox
    supl_id = tk.StringVar()
    tk.Label(window_supplier, text='Supplier Number:', font='Algerian', bg='white').place(x=550, y=150)
    tk.Entry(window_supplier, textvariable=supl_id, bd=3).place(x=750, y=155)

    # supplier_name and label, input box
    supl_name = tk.StringVar()
    tk.Label(window_supplier, text='Supplier Name:', font='Algerian', bg='white').place(x=550, y=250)
    tk.Entry(window_supplier, textvariable=supl_name, bd=3).place(x=750, y=255)

    # supl_company and label, input box
    supl_company = tk.StringVar()
    tk.Label(window_supplier, text='Supplier Company:', font='Algerian', bg='white').place(x=550, y=350)
    tk.Entry(window_supplier, textvariable=supl_company, bd=3).place(x=750, y=355)

    # Supplier location variable and label, input box
    supl_loc = tk.StringVar()
    tk.Label(window_supplier, text='Supplier Location:', font='Algerian', bg='white').place(x=550, y=450)
    tk.Entry(window_supplier, textvariable=supl_loc, bd=3).place(x=750, y=455)

    supl_phone_num = tk.StringVar()
    tk.Label(window_supplier, text='Phone Number:', font='Algerian', bg='white').place(x=550, y=550)
    tk.Entry(window_supplier, textvariable=supl_phone_num, bd=3).place(x=750, y=555)

    bt_submit = tk.Button(window_supplier, text='Submit', font='Algerian', bg='white', command=sign_to_oracle)
    bt_submit.place(x=630, y=650, width=200)

    window_supplier.mainloop()

# supplier_func()

# product_func()