from tkinter import *
from tkinter import ttk
#Setting up a raw layout
layout = Tk()
#Adding Textfield
#Entry is same as Textfield in java
Textfield = ttk.Entry(layout,width=50) #setting up the text field.
Textfield.pack() #pack function adds the Field in to the layout
#Adding Button to the layout
button = ttk.Button(layout,text="click me!")
button.pack()
def ButtonOnclick():
    print(Textfield.get()) #This function gets the entry and displays it on the console.
    Textfield.delete(0,END)#This deletes entry as it is created.
#The below function gives the command for the button to wht to do when the button is
#is clicked.    
    
button.config(command=ButtonOnclick) 
