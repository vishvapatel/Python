"""This program was asked in codevita 2018 i have solved it in python 3 and maybe my complexity is more but i have tried
The title is Base 6 in the question. If there is any simplest answer to the question the pls write to me """

n=int(input()) #taking input of the number of elemets of the array
inpt_string=input(); #taking input as a space seperated string
arr=[] #declaring array as a string
arr=inpt_string.split(" ") #spliting the string
i=0;
j=0
remlist=[] #this list will contain the sum of the elements convrted to base 6
while(i<n):
    j=int(arr[i])
    rem = 0                  #This loop is used for finding the sum of individual input elements after converting to base 6
    while(j>0):
        rem+= int(j % 6)
        j = j // 6
    remlist.append(rem)
    i=i+1
  #Below loop is used for counting the number of swaping required as requested
i=0
j=0
count=0
while(i<n):
    element=remlist[i]
    j=i
    while (j < n):
        if(element>remlist[j]):
            count+=1
        j+=1
    i+=1
print(count)        #printing the count variable which is final answer


