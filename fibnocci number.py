def fib(n):
    a=0
    b=1
    if n<0:
        print("cannot print fibnocci number")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
n=int(input("Enter the  range :- "))
fib(n)
