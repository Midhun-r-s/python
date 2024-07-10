num=int(input("Enter the number to check whether it is prime or not :- "))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not a prime number")
    else:
        print(num,"is prime number")
