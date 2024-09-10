def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b;

a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
print("Before Swap:",a," ",b)
a,b=swap(a,b)
print("After Swap:",a," ",b)
