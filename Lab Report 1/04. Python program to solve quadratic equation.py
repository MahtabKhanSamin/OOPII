a=int(input("Enter the Value for A:"))
b=int(input("Enter the Value for B:"))
c=int(input("Enter the Value for C:"))
s=pow((pow(b,2)-(4*a*c)),0.5)
a=2*a
b=-1*b
print("Either the Value of X is:")
print((b+s)/a)
print("or")
print((b-s)/a)
