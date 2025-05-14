from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle
#import oracle_connect
import cx_Oracle as cs
from PIL import ImageTk, Image

def enter_login():
    window_home.destroy()
    import login
    login.login_func()

window_home = tk.Tk()


window_home.title('HOME Page')
width = window_home.winfo_screenwidth()
height = window_home.winfo_screenheight()
window_home.geometry("%dx%d" % (width, height))

tk.image_home = ImageTk.PhotoImage(file="super_market.jpg")
tk.label = tk.Label(window_home, image=tk.image_home)
tk.label.pack()


bt_create = tk.Button(window_home, text='Login/Register', activebackground="gray", activeforeground='white',
                      fg='black', bg="#F0F8FF", font=("Arial", 15), command=enter_login)
bt_create.place(x=635, y=600, width=250)


window_home.mainloop()