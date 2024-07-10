n=int(input("Enter the number of rows :- "))
num=int(input("Enter the starting number :- "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print()
