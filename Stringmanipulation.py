str1=input("enteegrg")
total=0
lenth=0
list=str1.split()
for word in list:
    for letter in word:
        total=total+ord(letter)
    lenth=lenth+len(word)
avg=total/lenth
print(avg)
