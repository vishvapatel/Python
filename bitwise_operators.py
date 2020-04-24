x=0b101
y=0b100
z=input("Enter the operation")
if(z=="a"):
    m=x&y
    print('{:08b}'.format(m))
else:
    m=x|y
    print('{:08b}'.format(m))
