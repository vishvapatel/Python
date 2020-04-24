test=int(input())
fact=1
for i in range(test):
    number=int(input())
    for num in range(1,number+1):
        fact=fact*num
    print(fact)