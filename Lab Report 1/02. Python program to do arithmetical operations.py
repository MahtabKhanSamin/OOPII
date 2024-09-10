def ask():
    print("What do you want to do?")
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')
    return int(input());

a = int(input("Enter Your First Number:"))
b = int(input("Enter Your Second Number:"))
while 1:
    c=ask()
    if c>=1 and c<=4:
        break
    else:
        print("Wrong Input. Try Again.")
        continue

if c==1:
    print("Your Sum:",a+b)
elif c==2:
    print("Your Sub:",a-b)
elif c==3:
    print("Your Mul:",a*b)
elif c==4:
    print("Your Div:",a/b)
