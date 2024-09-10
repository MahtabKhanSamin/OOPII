def ask():
    print("What do you want to do?")
    print('1.Celsius to Fahrenheit')
    print('2.Fahrenheit to Celsius')
    print('3.Celsius to Kelvin')
    print('4.Fahrenheit to Kelvin')
    print('5.Kelvin to Fahrenheit')
    print('6.Kelvin to Celsius')
    return int(input());

while 1:
    c=ask()
    if c>=1 and c<=6:
        break
    else:
        print("Wrong Input. Try Again.")
        continue

if c==1:
    a=float(input("Enter The Temperature in Celsius:"))
    print("Your Temperature in Fahrenheit: %0.2f"%(32+(9*a/5)));
elif c==2:
    a = float(input("Enter The Temperature in Fahrenheit:"))
    print("Your Temperature in Celsius: %0.2f"%(5*(a-32)/9));
elif c==3:
    a = float(input("Enter The Temperature in Celsius:"))
    print("Your Temperature in Kelvin: %0.2f"%(a+273.15))
elif c==4:
    a = float(input("Enter The Temperature in Fahrenheit:"))
    print("Your Temperature in Kelvin: %0.2f"%((5*(a-32)/9)+273.15))
if c==5:
    a = float(input("Enter The Temperature in Kelvin:"))
    a=a-273.15
    print("Your Temperature in Fahrenheit: %0.2f"%(32+(9*a/5)))
if c==6:
    a = float(input("Enter The Temperature in Kelvin:"))
    print("Your Temperature in Celsius: %0.2f"%(a-273.15))
