num= int(input("Enter the number :- "))
i = 0
res = 0
while res < num :
    res = 1<<i
    if res==num:
        print("yes entered number is power of 2")
        break
    i=i+1
else:
    print("NO entered the number is not the power of 2")
