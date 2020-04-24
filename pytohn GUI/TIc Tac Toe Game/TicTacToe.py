#@author Vishva Patel
#Github Repository vishvapatel/python
#IDE used is Jetbrains Pycharm

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

#Global Variables------------------------------------------------------
Activeplayer =1
p1=[]
p2=[]
root=Tk()
root.title("Tic Tac Toe Player-1")
root.resizable(True,True)

#Styling the Layout
style = ttk.Style()
style.configure("TButton",background="Black",foreground="#00cc00",font=("Poppins" , 20))

# Defining Buttons ---------------------------------------------------
Bu1= ttk.Button(root,text=" ")
Bu1.grid(row=0,column=0,sticky="snew",ipadx=30,ipady=30)
Bu1.config(command=lambda: buclick(1))

Bu2= ttk.Button(root,text=" ")
Bu2.grid(row=0,column=1,sticky="snew",ipadx=30,ipady=30)
Bu2.config(command=lambda: buclick(2))

Bu3= ttk.Button(root,text=" ")
Bu3.grid(row=0,column=2,sticky="snew",ipadx=30,ipady=30)
Bu3.config(command=lambda: buclick(3))

Bu4= ttk.Button(root,text=" ")
Bu4.grid(row=1,column=0,sticky="snew",ipadx=30,ipady=30)
Bu4.config(command=lambda: buclick(4))

Bu5= ttk.Button(root,text=" ")
Bu5.grid(row=1,column=1,sticky="snew",ipadx=30,ipady=30)
Bu5.config(command=lambda: buclick(5))

Bu6= ttk.Button(root,text=" ")
Bu6.grid(row=1,column=2,sticky="snew",ipadx=30,ipady=30)
Bu6.config(command=lambda: buclick(6))

Bu7= ttk.Button(root,text=" ")
Bu7.grid(row=2,column=0,sticky="snew",ipadx=30,ipady=30)
Bu7.config(command=lambda: buclick(7))

Bu8= ttk.Button(root,text=" ")
Bu8.grid(row=2,column=1,sticky="snew",ipadx=30,ipady=30)
Bu8.config(command=lambda: buclick(8))

Bu9= ttk.Button(root,text=" ")
Bu9.grid(row=2,column=2,sticky="snew",ipadx=30,ipady=30)
Bu9.config(command=lambda: buclick(9))

#Defining Logic ----------------------------------------------------------------------------------------------

def buclick(id):
    global Activeplayer
    global p1
    global p2
    if Activeplayer == 1:
        setLayout(id,"X")
        root.title("Tic Tac Toe Player 2")
        Activeplayer =2
        p1.append(id)
        print("p1:{}".format(p1))
        AutoPlay()
    elif Activeplayer == 2:
        setLayout(id,"O")
        root.title("Tic Tac Toe Player 1")
        Activeplayer=1
        p2.append(id)
        print("p2:{}".format(p2))
    checkWinner()
def setLayout(id,playersymbol):
    if id == 1:
        Bu1.config(text=playersymbol)
        Bu1.state(["disabled"])
    elif id==2:
        Bu2.config(text=playersymbol)
        Bu2.state(["disabled"])
    elif id==3:
        Bu3.config(text=playersymbol)
        Bu3.state(["disabled"])
    elif id==4:
        Bu4.config(text=playersymbol)
        Bu4.state(["disabled"])
    elif id==5:
        Bu5.config(text=playersymbol)
        Bu5.state(["disabled"])
    elif id==6:
        Bu6.config(text=playersymbol)
        Bu6.state(["disabled"])
    elif id==7:
        Bu7.config(text=playersymbol)
        Bu7.state(["disabled"])
    elif id==8:
        Bu8.config(text=playersymbol)
        Bu8.state(["disabled"])
    elif id==9:
        Bu9.config(text=playersymbol)
        Bu9.state(["disabled"])

# Defining Rules----------------------------------------------------------------------------------------------
def checkWinner():
    winner=-1
    if ( (1 in p1) and (2 in p1) and (3 in p1)):
        winner = 1
    if (( 1 in p2 ) and (2 in p2) and (3 in p2)):
        winner = 2

    if ( (4 in p1) and (5 in p1) and (6 in p1)):
        winner = 1
    if (( 4 in p2 ) and (5 in p2) and (6 in p2)):
        winner = 2

    if ( (7 in p1) and (8 in p1) and (9 in p1)):
        winner = 1
    if (( 7 in p2 ) and (8 in p2) and (9 in p2)):
        winner = 2

    if ( (1 in p1) and (4 in p1) and (7 in p1)):
        winner = 1
    if (( 1 in p2 ) and (4 in p2) and (7 in p2)):
        winner = 2

    if ( (2 in p1) and (5 in p1) and (8 in p1)):
        winner = 1
    if (( 2 in p2 ) and (5 in p2) and (8 in p2)):
        winner = 2

    if ( (3 in p1) and (6 in p1) and (9 in p1)):
        winner = 1
    if (( 3 in p2 ) and (6 in p2) and (9 in p2)):
        winner = 2

    if ( (1 in p1) and (5 in p1) and (9 in p1)):
        winner = 1
    if (( 1 in p2 ) and (5 in p2) and (9 in p2)):
        winner = 2

    if ( (3 in p1) and (5 in p1) and (7 in p1)):
        winner = 1
    if (( 3 in p2 ) and (5 in p2) and (7 in p2)):
        winner = 2

    if winner == 1:
        messagebox.showinfo(title="Congratulations!",message="Player 1 is the Winner")

    if winner == 2:
        messagebox.showinfo(title="Congratulations!",message="Player 2 is the Winner")

def AutoPlay():
    global p1
    global p2
    Emptycells = []
    for cell in range(9):
        if (not((cell in p1) or (cell in p2))):
            Emptycells.append(cell)

    RandIndex= randint(0,len(Emptycells)-1)
    buclick(Emptycells[RandIndex])



root.mainloop()
