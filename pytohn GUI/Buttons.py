from tkinter import *
from tkinter import ttk
root_layout=Tk()
button=ttk.Button(root_layout,text="Click me!")
style = ttk.Style()
style.configure("TButton",background="#FFFFFF",foreground="#00cc00",font=("Helvetica",15,"bold"))
button.pack()
def OnclickButton():
    print("Button is clicked")
button.config(command=OnclickButton())
root_layout.mainloop()