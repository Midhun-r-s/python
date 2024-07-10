l1=[]
n=int(input("enter the size of list:- "))
for i in range(0,n):
    ele=input("Enter the list in integer form :- ")
    l1.append(ele)
print("The list before reversal :- ",l1)
rev=l1[::-1]
print("The reversed list is:- ",rev)
