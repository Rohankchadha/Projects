a=int(input("enter number"))
factorial=1
for i in range(1,a+1):
    fact=factorial*i
    factorial=fact
print(fact)
