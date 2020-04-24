list=[101,50,1,100,45,12]
i=0
max=0
min=list[0]
while(i<6):
  
    if(max<list[i]):
        max=list[i]
        
    
    if(min>list[i]):
        min=list[i]

    i=i+1

print("The maximum number in the list is :",max)
print("The minimum number in the liat is :",min)
