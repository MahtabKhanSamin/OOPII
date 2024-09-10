a=int(input("Enter the Year: "))
if a%4==0 and a%400==0 or a%100!=0:
    print("The Year is a Leap Year")
else:
    print("The Year is NOT a leap Year")