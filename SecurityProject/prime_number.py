a=int(input("enter a number : "))
if(a>1):
    for i in range(2,a):
        if(a%i==0):
            print("not a prime number")
            break
        else:
            print("prime number")
            break
elif(a==1):
    print("prime number")
elif(a==0):
    print("Number is Zero")
else:
    print("enter positive number")