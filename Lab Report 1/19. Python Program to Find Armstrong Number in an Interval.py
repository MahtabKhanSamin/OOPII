def checkarm(a):
    b = a
    sum = 0
    while a != 0:
        sum = sum + pow((a % 10), 3)
        a = int(a / 10)
    if sum == b:
        return 1
    else:
        return 0

x=int(input("Enter The Range:\nFrom:"))
y=int(input("To:"))
for z in range(x,y+1):
    c=checkarm(z)
    if c==1:
        print(z)
    else:
        continue