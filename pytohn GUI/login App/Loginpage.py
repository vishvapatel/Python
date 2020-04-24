from tkinter import *
from tkinter import ttk
from tkinter import messagebox
layout = Tk()
layout.resizable(False,False)
layout.title("Login")
def BUclick():
    if( (userentry.get())=="admin" and (passwentry.get())=="1234"):
        messagebox.showinfo(title="Login Info",message="Welcome! to Python app")
        userentry.delete(0, END)
        passwentry.delete(0, END)
    else:
        messagebox.showinfo(title="Login Info",message="Invalid Username or Password")

username=Label(layout,text="Username").grid(row=0,column=0,padx=5,pady=5,sticky="E")
password=Label(layout,text="Password").grid(row=1,column=0,padx=5,pady=5,sticky="E")
userentry=ttk.Entry(layout,background="#000000",foreground="#00cc00")
userentry.grid(row=0,column=1,padx=2,ipadx=2)
passwentry=ttk.Entry(layout,background="#000000",foreground="#00cc00")
passwentry.grid(row=1,column=1,padx=2,ipadx=2)
passwentry.config(show="*")
check= ttk.Checkbutton(layout,text="Keep me logged in")
check.grid(row=2,column=1,padx=2,pady=2,sticky="ew")
loginbut=ttk.Button(layout,text="Login",command=BUclick)
loginbut.grid(row=3,column=1)

layout.mainloop()
