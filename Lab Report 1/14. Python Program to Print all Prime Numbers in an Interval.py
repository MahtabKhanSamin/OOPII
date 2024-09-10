print("Enter Your Range:")
a = int(input("From: "))
b = int(input("To: "))
print("Your Prime Numbers are: ")
for x in range(a,b+1):
    if x>1:
        for y in range(2,int(x/2)+1):
            if(x%y)==0:
                break;
        else:
            print(x)