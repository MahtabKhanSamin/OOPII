def ask():
    print("What do you want to do?")
    print('1.KM to Miles')
    print('2.Miles to KM')
    return int(input());

while 1:
    c=ask()
    if c>=1 and c<=2:
        break
    else:
        print("Wrong Input. Try Again.")
        continue

if c==1:
    a=float(input("Enter The Distance in KM:"))
    print("Your Distance in Miles: %0.2f"%(a/1.60934))
elif c==2:
    a = float(input("Enter The Distance in Miles:"))
    print("Your Distance in KM: %0.2f"%(a*1.60934))
