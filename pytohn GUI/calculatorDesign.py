# This is a calclator in python GUI Applications
from tkinter import *
from tkinter import ttk

layout = Tk()
layout.title("Calculator")
layout.resizable(False, False)
style = ttk.Style()
style.theme_use("winnative")
style.configure("TButton", background="#000000", foreground="#00cc00", font=("Courier New", 15))


# --------------------------Main Logic Goes Here -------------------------------------------------------------

# Adding OnClick Functions to Buttons

def BUClick(id):
    IOentry.insert(END, id)


def BUdot():
    IOentry.insert(END, ".")


def clear():
    IOentry.delete(0, END)


def add():
    IOentry.insert(END, "+")


def sub():
    IOentry.insert(END, "-")


def mul():
    IOentry.insert(END, "*")


def div():
    IOentry.insert(END, "/")


def BUOutput():
    IOentry.delete(0, END)
    IOentry.insert(0, "Coming Soon")


# Design Begins------------------------------------------------------------------------------------------------

title = Label(layout, text="Calculator", background="#000000", foreground="#00cc00", font=("Courier New", 24))
title.grid(row=0, column=0, columnspan=4, ipadx=2, ipady=2, sticky="ew")

# Where It's All Seen------------------------------------------------------------------------

IOentry = ttk.Entry(layout, font=("Courier New", 18))
IOentry.grid(row=1, column=0, columnspan=4, padx=5, pady=5, ipadx=3, ipady=3, sticky="ew")

# Taking Input Buttons------------------------------------------------------------

but7 = ttk.Button(layout, text="7")
but7.grid(row=2, column=0, ipadx=2, ipady=2)
but7.config(command=BUClick("7"))

but8 = ttk.Button(layout, text="8")
but8.grid(row=2, column=1, ipadx=2, ipady=2)
but8.config(command=BUClick("8"))

but9 = ttk.Button(layout, text="9")
but9.grid(row=2, column=2, ipadx=2, ipady=2)
but9.config(command=BUClick("9"))

but4 = ttk.Button(layout, text="4")
but4.grid(row=3, column=0, ipadx=2, ipady=2)
but4.config(command=BUClick("4"))

but5 = ttk.Button(layout, text="5")
but5.grid(row=3, column=1, ipadx=2, ipady=2)
but5.config(command=BUClick("5"))

but6 = ttk.Button(layout, text="6")
but6.grid(row=3, column=2, ipadx=2, ipady=2)
but6.config(command=BUClick("6"))

but1 = ttk.Button(layout, text="1")
but1.grid(row=4, column=0, ipadx=2, ipady=2)
but1.config(command=BUClick("1"))

but2 = ttk.Button(layout, text="2")
but2.grid(row=4, column=1, ipadx=2, ipady=2)
but2.config(command=BUClick("2"))

but3 = ttk.Button(layout, text="3")
but3.grid(row=4, column=2, ipadx=2, ipady=2)
but3.config(command=BUClick("3"))

but0 = ttk.Button(layout, text="0")
but0.grid(row=5, column=0, rowspan=2, ipadx=2, ipady=2, sticky="sn")
but0.config(command=BUClick("0"))

butdot = ttk.Button(layout, text=".")
butdot.grid(row=5, column=1, rowspan=2, ipadx=2, ipady=2, sticky="sn")
butdot.config(command=BUdot)

butoutput = ttk.Button(layout, text="=")
butoutput.grid(row=5, column=2, rowspan=2, ipadx=2, ipady=2, sticky="sn")
butoutput.config(command=BUOutput)

# Operators Buttons--------------------------------------------------------------------

clearbut = ttk.Button(layout, text="Clear", command=clear)
clearbut.grid(row=2, column=3, ipadx=2, ipady=2)

divbut = ttk.Button(layout, text="/", command=div)
divbut.grid(row=3, column=3, ipadx=2, ipady=2)

mulbut = ttk.Button(layout, text="*", command=mul)
mulbut.grid(row=4, column=3, ipadx=2, ipady=2)

subbut = ttk.Button(layout, text="-", command=sub)
subbut.grid(row=5, column=3, ipadx=2, ipady=2)

addbut = ttk.Button(layout, text="+", command=add)
addbut.grid(row=6, column=3, ipadx=2, ipady=2)

layout.mainloop()
