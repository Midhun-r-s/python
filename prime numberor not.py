a=int(input("Enter the number you want to check  :- "))
count=0
for i in range(2,a):
    if a%i==0:
        print(a,"is Not a prime number")
        break
else:
    print(a," is a prime number")
        
