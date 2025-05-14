import Create
from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle
# import oracle_connect
import cx_Oracle as cs
from PIL import ImageTk, Image

import login
import R_CPS
import Crud_Op
from tkinter.ttk import Combobox
import sys

from twilio.rest import Client


con = cs.connect('name/password@localhost')
cur = con.cursor()

def read_func():

    class Test:
        def __init__(self, tk):
            self.var = StringVar()

            self.label2 = Label(tk, text='Sample SMS', font='Algerian').place(x=850, y=20)

            self.image_login = ImageTk.PhotoImage(file="msg_image.jpg")
            self.label = Label(tk, image=self.image_login).place(x=850,y=50)


            self.label1 = Label(tk, text='Select the option:',font='Algerian').place(x=200, y=250)
            self.data = ("Product", "Category", "Supplier","Employee")
            self.cb = Combobox(tk, values=self.data)
            value = self.cb.get()
            self.cb.place(x=380, y=250)
            self.b1 = Button(tk, text="Read", command=self.select).place(x=310, y=330, width=150)

            '''
            self.label1 = Label(tk, text='Select the option:', font='Algerian').place(x=550, y=400)
            var_id = StringVar()
            self.entry = Entry(tk, textvariable=var_id, font='Algerian').place(x=750, y=400)
            #print(self.cb,self.label,self.data,self.b1,self.var)
            '''

        def select(self):
            value = self.cb.get()
            #print(value)
            if(value == "Product"):
                R_CPS.products()
            if(value == "Category"):
                R_CPS.category()
            if(value == "Supplier"):
                R_CPS.supplier()
            if(value == "Employee"):
                R_CPS.employee()
            #messagebox.showinfo("Xiith.com", "You selected " + value)


    tk = Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.geometry("%dx%d" % (width, height))
    tk.title("READ page")
    tt = Test(tk)

    def call_crud():
        tk.destroy()
        Crud_Op.crud_func()


    def call_login():
        tk.destroy()
        Login.login_func()

    menubar = Menu(tk)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Back", command=call_crud)

    filemenu.add_separator()

    filemenu.add_command(label="Logout", command=call_login)
    menubar.add_cascade(label="Menu", menu=filemenu)

    tk.config(menu=menubar)

    tk.mainloop()




def call_otp():
    try:

        con = cs.connect('name/password@localhost')
        cur = con.cursor()
        # Creating a table srollno heading which is number

        cur.execute("select prod_name,quantity from product_table")

        result = [dict(line) for line in
                  [zip([column[0] for column in cur.description], row) for row in cur.fetchall()]]
        print(result) #
        print(type(result)) #
        data = []
        for i in result:
            print(type(i)) #
            print(i.keys(),i.values()) #
            for j in i:
                data.append(i[j])

        result=[]
        for i in range(1, len(data), 2):
            if(data[i]==0):
                result.append(data[i-1])
                #result.append(data[i])
        print(result)

        list_sid = ['id']
        list_token = ['token']
        list_from_phone = ['twiliomobileno']
        list_to_phone = ['mobileno']

        for i in range(len(list_sid)):
            print(list_sid[i], list_token[i])
            client = Client(list_sid[i], list_token[i])
            print(list_from_phone[i], list_to_phone[i])
            message = client.messages \
                .create(
                body='Products not available in the store are \n' + str(result),
                from_=list_from_phone[i],
                to=list_to_phone[i]
                )


    # by writing finally if any error occurs
    # then also we can close the all database operation

    except cs.DatabaseError as e:
        print("There is a problem with Oracle", e)

    finally:
        if cur:
            cur.close()
        if con:
            con.close()


def delete_func():
    con = cs.connect('name/password@localhost')
    cur = con.cursor()

    window_delete = tk.Tk()
    window_delete.title('Delete')
    width = window_delete.winfo_screenwidth()
    height = window_delete.winfo_screenheight()
    window_delete.geometry("%dx%d" % (width, height))

    tk.image_home = ImageTk.PhotoImage(file="cart_image.jpg")
    tk.label = tk.Label(window_delete, image=tk.image_home)
    tk.label.pack()

    def call_crud():
        window_delete.destroy()
        Crud_Op.crud_func()
    def call_login():
        window_delete.destroy()
        Login.login_func()

    menubar = Menu(window_delete)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Back", command=call_crud)

    filemenu.add_separator()

    filemenu.add_command(label="Logout", command=call_login)
    menubar.add_cascade(label="Menu", menu=filemenu)

    window_delete.config(menu=menubar)

    def call_p_id():
        new_p_id = var_p_id.get()

        sql_delete_product = "delete from product_table where prod_id='{}'".format(new_p_id)

        cur.execute("select prod_id from product_table where prod_id = '{}'".format(new_p_id))
        row = cur.fetchall()

        if (row != []):
            if (new_p_id == ''):
                tk.messagebox.showerror('error', 'Number is required')
            else:
                cur.execute(sql_delete_product)
                con.commit()
                tk.messagebox.showinfo('welcome', 'Product deleted!!!')

    def call_c_id():
        new_c_id = var_c_id.get()

        sql_delete_category = "delete from category_table where category_id='{}'".format(new_c_id)

        cur.execute("select category_id from category_table where category_id = '{}'".format(new_c_id))
        row = cur.fetchall()

        if (row != []):
            if (new_c_id == ''):
                tk.messagebox.showerror('error', 'Number is required')
            else:
                cur.execute(sql_delete_category)
                con.commit()
                tk.messagebox.showinfo('welcome', 'Category deleted!!!')

    def call_s_id():
        new_s_id = var_s_id.get()

        sql_delete_supplier = "delete from supplier_table where supl_id='{}'".format(new_s_id)

        cur.execute("select supl_id from supplier_table where supl_id = '{}'".format(new_s_id))
        row = cur.fetchall()

        if (row != []):
            if (new_s_id == ''):
                tk.messagebox.showerror('error', 'Number is required')
            else:
                cur.execute(sql_delete_supplier)
                con.commit()
                tk.messagebox.showinfo('welcome', 'Supplier deleted!!!')

    var_p_id = tk.StringVar()
    tk.Label(window_delete, text='Enter Product Number:', font=("Algerian", 15), bg='white', fg='black').place(x=500,
                                                                                                                 y=200)
    tk.Entry(window_delete, textvariable=var_p_id, font=("times new roman", 15),bd=3).place(x=720, y=200, width=250)

    bt_submit = tk.Button(window_delete, text='Delete', bg="#F0F8FF", font=("Algerian", 10), command=call_p_id).place(
        x=710, y=255,
        width=100)
    var_c_id = tk.StringVar()
    tk.Label(window_delete, text='Enter Category Number:', font=("Algerian", 15), bg='white', fg='black').place(x=500,
                                                                                                                  y=300)
    tk.Entry(window_delete, textvariable=var_c_id, font=("times new roman", 15),bd=3).place(x=720, y=300, width=250)

    bt_submit1 = tk.Button(window_delete, text='Delete', bg="#F0F8FF", font=("Algerian", 10), command=call_c_id).place(
        x=710, y=355,
        width=100)

    var_s_id = tk.StringVar()
    tk.Label(window_delete, text='Enter Supplier Number:', font=("Algerian", 15), bg='white', fg='black').place(x=500,
                                                                                                                  y=400)
    tk.Entry(window_delete, textvariable=var_s_id, font=("times new roman", 15),bd=3).place(x=720, y=400, width=250)

    bt_submit2 = tk.Button(window_delete, text='Delete', bg="#F0F8FF", font=("Algerian", 10), command=call_s_id).place(
        x=710, y=455,
        width=100)
    
    window_delete.mainloop()


#delete_func()
#call_otp()
#read_func()
