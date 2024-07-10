def input1():
    a=int(input("Enter the first number:- "))
    b=int(input("Enter the second number :- "))
    c=add(a,b)
def add(a,b):
    s=a+b
    print(f"The sum before adding 5 :- {s}")
    d=s+5
    print(f"The sum after adding 5 :- {d}")
    
input1()
