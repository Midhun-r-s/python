string=input("Enter the string you want to reverse :- ")
l1=[]
for i in string:
    l1.append(i)
print("The string before revresal :- ",l1)
rev=l1[::-1]
print("The list for reversed string is :- ",rev)
