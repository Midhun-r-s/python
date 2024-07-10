l1=[]
n=int(input("Enter the size of string:- "))
for i in range(0,n):
    ele=int(input("Enter the elements in integer form :- "))
    if ele%2==0:
        l1.append(ele)
    else:
        print("There are no even numbers in the list :(")
    
print("The even numbers in the list are :- ",l1)

