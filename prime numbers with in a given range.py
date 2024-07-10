r=int(input("Enter the range to find out prime numbers :- "))
print("The prime numbers are :- ")
for i in range(1,r+1):
    num=i
    if num>1:
        for j in range(2,num):
            if (num%j)==0:
                break
        else:
            print(num)
