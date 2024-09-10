a=int(input("Enter Your Number: "))
if a<2:
    print("Your Number is NOT Prime")
else:
    for x in range(2,int(a/2)+1):
        if a%x==0:
            print("Your Number is NOT Prime")
            break;
    else:
        print("Your Number is Prime")
