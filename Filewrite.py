def main(): #defining the main function
    out=open("test.txt","a")#opening the fileif file is not created then it will create the file
    out.write("\nCool!")#appending the file means adding the text to the file
    out.close() #closing the file
    f = open("test.txt", "a")
    for i  in range(5):
        inputtofile=input("Enter the string to the file:")#taking input form the use rto add in the file
        f.write("\n{}".format(inputtofile))#assigining the variable the file write
    f.close()#closing the file




if __name__ == '__main__':main()