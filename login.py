from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle
# import oracle_connect
import cx_Oracle as cs
from PIL import ImageTk, Image


def login_func():
    # Database connection
    #cs.init_oracle_client(lib_dir="/path/to/oracle/client/lib")
    con = cs.connect('nandini/123456@localhost')
    cur = con.cursor()

    # Window
    window = tk.Tk()
    window.title('Login Page')
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry("%dx%d" % (width, height))

    #### creating image on window####
    tk.image_login = ImageTk.PhotoImage(file="login_img.jpg")
    tk.label = tk.Label(window, image=tk.image_login)
    tk.label.pack()

    '''
    #### Creating frame  on root window ####
    tk.frame = tk.Frame(window)
    tk.frame.place(x=550, y=150, width=400, height=450)

    '''

    # Label Username on frame
    enter_email = tk.Label(window, text='E-mail:', font=("Algerian", 15), bg='#F0F8FF', fg='black')
    enter_email.place(x=580, y=200)

    # Usermail input box on frame
    var_usr_mail = tk.StringVar()
    entry_usr_mail = tk.Entry(window, textvariable=var_usr_mail, font=("times new roman", 15), bd=5)
    entry_usr_mail.place(x=580, y=250, width=250)

    # Label password on frame
    enter_passw = tk.Label(window, text='Password:', font=("Algerian", 15), bg='#F0F8FF', fg='black')
    enter_passw.place(x=580, y=300)

    # Password input box on frame
    var_usr_pwd = tk.StringVar()
    entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*', font=("times new roman", 15), bd=5)
    entry_usr_pwd.place(x=580, y=350, width=250)

    # Login function
    def usr_log_in():

        # Input box to get username and password
        # usr_id = var_usr_id.get()
        usr_mail = var_usr_mail.get()
        usr_pwd = var_usr_pwd.get()

        # Get user information from the database
        # sql = "select * from signin where email= '%s'" %usr_name
        cur.execute("select * from login_table where emp_username='{}'".format(usr_mail))
        row = cur.fetchall()
        # print(row)

        # Check if there is a username
        if (row != []):
            # Determine whether the password matches
            if (row[0][2] == str(usr_pwd)):
                # tk.messagebox.showinfo(title='welcome',message='Welcome'+usr_mail)
                window.destroy()
                import Crud_Op
                Crud_Op.crud_func()

            else:
                tk.messagebox.showerror(message='wrong password')
        # check whether it is empty
        elif usr_mail == '' or usr_pwd == '':
            tk.messagebox.showerror(message='usermail or password is empty')
        else:
            is_signup = tk.messagebox.askyesno('welcome', 'You have not registered yet, do you want to register now? ')
            ######print(is_signup)
            if is_signup:
                usr_sign_up()

    # Registration function
    def usr_sign_up():
        def sign_to_oracle():
            new_i_d = new_id.get()
            new_n = new_name.get()
            new_ph_n = new_phone_num.get()
            new_e = new_mail.get()  # mail;
            new_p = new_pwd.get()
            new_p_c = new_pwd_confirm.get()

            # sql_select = "select email from signin where email = '{}'".format(new_e)
            sql_insert_login = "insert into login_table(emp_id,emp_username,password) values('{}','{}','{}')".format(
                new_i_d, new_e, new_p)

            sql_insert_signup = "insert into employee_table(emp_id,emp_name,phone_number) values('{}','{}','{}')".format(
                new_i_d, new_n, new_ph_n)

            cur.execute("select emp_username from login_table where emp_username = '{}'".format(new_e))
            row = cur.fetchall()
            # print(row)

            if (row == []):
                if (new_i_d == '' or new_n == '' or new_ph_n == '' or new_e == '' or new_p == '' or new_p_c == ''):
                    tk.messagebox.showerror('error', 'All fields are required')
                elif (new_p != new_p_c):
                    tk.messagebox.showerror('error', 'Passwords are inconsistent before and after')
                else:
                    cur.execute(sql_insert_login)
                    cur.execute(sql_insert_signup)
                    con.commit()
                    tk.messagebox.showinfo('welcome', 'Registration Success!!!')

                    # Register successfully close the registration box
                    window_sign_up.destroy()

            else:
                tk.messagebox.showerror('error', 'Usermail already exists')

        # New registration page
        window_sign_up = tk.Toplevel(window)
        window_sign_up.geometry('600x400')
        window_sign_up.title('Registeration')

        # user employe_id and label, inputbox
        new_id = tk.StringVar()
        tk.Label(window_sign_up, text='Employee Number:').place(x=10, y=10)
        tk.Entry(window_sign_up, textvariable=new_id).place(x=150, y=10)

        # User name variable and label, input box
        new_name = tk.StringVar()
        tk.Label(window_sign_up, text='Name:').place(x=10, y=50)
        tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=50)

        # User name variable and label, input box
        new_phone_num = tk.StringVar()
        tk.Label(window_sign_up, text='Phone Number:').place(x=10, y=90)
        tk.Entry(window_sign_up, textvariable=new_phone_num).place(x=150, y=90)

        # User E-mail variable and label, input box
        new_mail = tk.StringVar()
        tk.Label(window_sign_up, text='E-mail:').place(x=10, y=130)
        tk.Entry(window_sign_up, textvariable=new_mail).place(x=150, y=130)

        # Password variables and labels, input boxes
        new_pwd = tk.StringVar()
        tk.Label(window_sign_up, text='Password:').place(x=10, y=170)
        tk.Entry(window_sign_up, textvariable=new_pwd).place(x=150, y=170)

        # Repeat password variables and labels, input boxes
        new_pwd_confirm = tk.StringVar()
        tk.Label(window_sign_up, text='Retype Password:').place(x=10, y=210)
        tk.Entry(window_sign_up, textvariable=new_pwd_confirm).place(x=150, y=210)

        # Confirm registration button and location
        bt_confirm_sign_up = tk.Button(window_sign_up, text='Confirm Registration', command=sign_to_oracle)
        bt_confirm_sign_up.place(x=150, y=250)

    # Exit function
    def usr_sign_quit():
        window.destroy()
        con.commit()
        con.close()

    # Login and register button
    bt_log_in = tk.Button(window, text='Login', bg="#F0F8FF", font=("Algerian", 15), command=usr_log_in).place(x=630,
                                                                                                               y=400,
                                                                                                               width=150)
    bt_sign_up = tk.Button(window, text='Register', bg="#F0F8FF", font=("Algerian", 15), command=usr_sign_up).place(
        x=580, y=480,
        width=250)
    bt_quit = tk.Button(window, text='Exit', bg="#F0F8FF", font=("Algerian", 15), command=usr_sign_quit).place(x=580,
                                                                                                               y=550,
                                                                                                               width=250)

    window.mainloop()

# login_func()