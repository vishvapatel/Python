hours=int(input("Enter the hours worked :"))
rate=float(input("Enter the rate per hour:"))
if(hours<40):
    income=hours*rate
    print("Your income is:",income)
if(hours>40):
    Extra=hours-40
    newrate=rate*1.5
    income=(40*rate)+(Extra*newrate)
    print("Your income is:",income)

