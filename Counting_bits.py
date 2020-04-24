n=int(input()) #taking input of number of elements
#count bits program
string=input() #taking array as string
arr=[] # taking list
arr=string.split(",")#splitting the string array
#converting the decimal to binary loops
i=0
j=0
brr=[]
while(i<n):
    j=int(arr[i])
    c=0
    while(j>=1):
        if (int(j)%2 != 0):   
            c=c+1
        j=int(j/2)
    brr.insert(i,c)
    i=i+1
#sorting the  number of 1's combination loops
m=0
i=0
count=0
while(i<n):
    j=i
    m=brr[i]
    while(j<n):
       
        if(m > brr[j]):
            count=count+1
        j=j+1
    i=i+1

#printing the count
print(count)
    








