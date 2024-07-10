while True:
    a=int(input("Enter the first number :- "))
    b=int(input("Enter the second number :- "))
    print("\n1. ADDITION\n2. SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.REMAINDER\n")
    c=int(input("Enter the choice from the Menu :- "))
    

    if c==1:
        sum=a+b
        print("The sum  of",a,"and",b,"is :- ",sum)
    elif c==2:
        if a>b:
            diff=a-b
            print("The difference  of",a,"and",b,"is :- ",diff)
        else:
            diff=b-a
            print("The sum  of",b,"and",a,"is :- ",diff)
            print("Here 'b' is greater than 'a' so the operation is b-a")
    elif c==3:
        pro=a*b
        print("The product of",a,"and",b,"is :- ",pro)
    elif c==4:
        quo=a/b
        print("The quotient of",a,"and",b,"is :- ",quo)
    elif c==5:
        rem=a%b
        print("The remiander of",a,"and",b,"is :- ",rem)
    else:
        print("Invalid choice")

    ans=input("do you want to continue?(y/n) :- ")
    ans=ans.lower()
    if ans == 'n':
        print("Thank you")
        break
    

    
