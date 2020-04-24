n=int(input("Enter the number"))
i=1
fact=1
while(i<=n):
    if(n==0):
        print(n)
    else:
        fact=fact*i
        i=i+1
print(fact)
