a=int(input("How many numbers do you want: "))
b=0
c=1
print(b,c,end=" ")
for x in range(2,a):
    d=b+c
    print(d,end=" ")
    b=c
    c=d