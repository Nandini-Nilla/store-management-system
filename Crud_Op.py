from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle
# import oracle_connect
import cx_Oracle as cs
from PIL import ImageTk, Image
from datetime import datetime
import Read_Delete
import Update
import Create
import login



def crud_func():
    con = cs.connect('name/password@localhost')
    cur = con.cursor()


    def call_create():
        window_crud.destroy()
        Create.create_func()

    def call_update():
        window_crud.destroy()
        Update.update_func()

    def call_read():
        window_crud.destroy()
        Read_Delete.read_func()

    def call_delete():
        window_crud.destroy()
        Read_Delete.delete_func()

    def call_otp():
        #window_crud.destroy()
        Read_Delete.call_otp()
        tk.messagebox.showinfo('welcome', 'MESSSAGE SENT!!!')

    def call_login():
        window_crud.destroy()
        Login.login_func()



    window_crud = tk.Tk()
    window_crud.title('CRUD Page')
    #window_crud.geometry("600x700+288+78")

    width = window_crud.winfo_screenwidth()
    height = window_crud.winfo_screenheight()
    window_crud.geometry("%dx%d" % (width, height))

    menubar = Menu(window_crud)
    filemenu = Menu(menubar, tearoff=0)

    filemenu.add_command(label="Exit", command=call_login)
    menubar.add_cascade(label="Logout", menu=filemenu)

    window_crud.config(menu=menubar)

    tk.image_crud = ImageTk.PhotoImage(file="crud_image.jpg")
    tk.label = tk.Label(window_crud, image=tk.image_crud)
    tk.label.pack()



    cur.execute("SELECT prod_id,prod_name,prod_expiry_date from product_table")

    ### stores the query data in dictionary format#####
    result = [dict(line) for line in
              [zip([column[0] for column in cur.description], row) for row in cur.fetchall()]]
    # print(result)
    ### converting dictionary into list #####
    data = []
    for i in result:
        # print(type(i))
        # print(i.keys(),i.values())
        for j in i:
            data.append(i[j])
    # print(data)

    # dictinary to display expiry products #####
    dict_s = {}
    count = 0
    for i in range(2, len(data), 3):
        p_e_d = data[i]
        v_p_e_d = p_e_d.date()
        today_date = datetime.now()
        curr_date = today_date.date()
        if (v_p_e_d == curr_date):
            count = count + 1
            # print(data[i - 2])
            # print(data[i - 1])
            dict_s[data[i - 2]] = data[i - 1]
            # dict_s.value(data[i-1])

    if (count != 0):
        s = tk.messagebox.showinfo('EXPIRY DATES OF PRODUCTS', dict_s)
        print(s)
    def call_exp_date():
        try:
            if s:
                window_crud.destroy()
                import info_expiry_date
                info_expiry_date.i_e_d_func(dict_s)
        except NameError:
            tk.messagebox.showinfo('Expiry','No Expired Products')



    bt_create = tk.Button(window_crud, text='Create', activebackground="gray", activeforeground='white',
                          fg='black', bg='SkyBlue1', font=("Arial", 15),bd=3,command=call_create)
    bt_create.place(x=550, y=100, width=250)

    bt_update = tk.Button(window_crud, text='Update', activebackground="gray", activeforeground='white',
                          fg='black', bg='SkyBlue1', font=("Arial", 15),bd=3,command=call_update)
    bt_update.place(x=550, y=200, width=250)


    bt_read = tk.Button(window_crud, text='Read', activebackground="gray", activeforeground='white',
                        fg='black', bg='SkyBlue1', font=("Arial", 15),bd=3,command=call_read)
    bt_read.place(x=550, y=300, width=250)


    bt_delete = tk.Button(window_crud, text='Delete', activebackground="gray", activeforeground='white',
                          fg='black', bg='SkyBlue1', font=("Arial", 15),bd=3,command=call_delete)
    bt_delete.place(x=550, y=400, width=250)

    bt_exp_date = tk.Button(window_crud, text='Expiry Date', activebackground="gray", activeforeground='white',
                          fg='black', bg='SkyBlue1', font=("Arial", 15), bd=3,command=call_exp_date)
    bt_exp_date.place(x=550, y=500, width=250)

    bt_otp = tk.Button(window_crud, text='Send SMS', activebackground="gray", activeforeground='white',
                            fg='black', bg='SkyBlue1', font=("Arial", 15), bd=3, command=call_otp)
    bt_otp.place(x=550, y=600, width=250)


    window_crud.mainloop()


#crud_func()