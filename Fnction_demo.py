"""we are making a calculator as an example of demonstrating a python functions"""
def sum( x,y):
    result=x+y
    print("sum is {}".format(result))
def sub(x,y):
    result=x-y
    print("Subtraction is {}".format(result))
def mul(x,y):
    result=x*y
    print("Multiplication  is {}".format(result))
def div(x,y):
    result=x/y
    print("Division is {}".format(result))
def modulus(x,y):
    result=x%y
    print("Modulus is {}".format(result))

#--the main function--------------------------
def main():
 x=int(input("Enter the first number"))
 y=int(input("ENter the Second number"))
 choice=input("Enter your choice:\n add ofr addition \n sub for subtraction \n mul for multiplication \n div for division \n mod for modulus")
 if(choice=="add"):
     sum(x,y)
 elif(choice=="sub"):
     sub(x,y)
 elif(choice=="div"):
     div(x,y)
 elif(choice=="mod"):
     modulus(x,y)
 elif(choice=="mul"):
     mul(x,y)
 else:
     print("OOPS!!! you didn't Enter the choice")

if __name__=="__main__":main()
