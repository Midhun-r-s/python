
def fib(n):
    
    a=0
    b=1
    print(a,end=" ")
    print(b,end=" ")
    for i in range(1,n):
            c=a+b
            a=b
            b=c
            print(c,end=" ")



n=int(input("enter the number of times : "))
fib(n)
