list=[]
n=int(input("Enter the number of Elements :- "))
for i in range(0,n):
    ele=int(input("Enter the elements :- "))
    if ele%2==0:
        list.append(ele)
print("Even number list :- ",list)
