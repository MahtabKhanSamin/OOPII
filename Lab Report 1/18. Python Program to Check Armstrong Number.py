a=int(input("Enter Your Number: "))
b=a
i=0
sum=0
while a!=0:
    sum=sum+pow((a%10),3)
    a=int(a/10)

if sum==b:
    print("Your Number is a Armstrong Number")
else:
    print("Your Number is NOT a Armstrong Number")