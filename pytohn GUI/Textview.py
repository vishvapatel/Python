from tkinter import *
from tkinter import ttk 

def ButOnClick():
    name=Tf.get()
    Ta.insert(END,"Welcome!"+name)
    Tf.delete(0,END)
    

layout=Tk()
Tf=ttk.Entry(layout,width=50)
Tf.insert(0,"Enter your name")
Tf.pack()
Ta = Text(layout,height=10,width=50)
Ta.pack()
button=ttk.Button(layout,text="NEXT>")
button.config(command=ButOnClick)
button.pack()
style = ttk.Style()
style.theme_use('clam')
style.configure("TButton",foreground = "green",background = "white",font = ("Arial",16,"italic"))



    
    
    
