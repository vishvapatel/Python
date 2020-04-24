n=12
print("LET'S PLAY GUESS THE NUMBER YOU HAVE THREE CHANCES TO GUESS THE INPUTED NUMBER")
i=0
while(1):
    i=i+1
    if(i>3):
        break

    print(i,"chance")
    m=int(input("Enter the number :"))
   
    if(m > n):
        print("YOU ARE GREATER THAN THE NUMBER TRY AGAIN!!!")
        
    elif(m < n):
        print("YOU ARE SMALLER THAN THE NUMBER TRY AGAIN!!!")
       
        
    else:
        print("YAAY!! YOU HIT THE BULL'S EYE")
        print("THE NUMBER IS",m)
        break

if(m!=n and i==4):
    print(" SORRY WANNA PLAY AGAIN!!! RERUN THE PROGRAM ")
