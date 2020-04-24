"""This is a program to calculate the fine by a car in a month at any date condition is if the date
                                    is odd then fine would be taken of the even number cars.
                                    QUESTION OF MICROSOFT CORPORATION
                                    Source: Geekforgeeks"""

test=int(input())
for j in range(test):
    number_string=input()
    number=[]
    number=number_string.split(" ")
    num=int(number[0])
    date=int(number[1])
    car_num=[]
    car_num_string=input()
    car_num=car_num_string.split(" ")
    penalty=[]
    penalty_string=input()
    penalty=penalty_string.split(" ")
    #iteration for checking the fine
    fine=0
    for i in range (num):
        if(date%2==0):
            if(int(car_num[i])%2!=0):
                fine=fine+int(penalty[i])
        else:
            if(int(car_num[i])%2==0):
                fine=fine+int(penalty[i])
    print(fine)
