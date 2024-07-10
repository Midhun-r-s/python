string=input("Enter the string you want to slice :- ")
l1=[]
j=int(input("Enter the starting index :- "))
k=int(input("Enter the ending index :- "))
sliced=string[j:k+1:1]
for i in sliced:
    l1.append(i)
print(f"The sliced word from the input word '{string}' is :-",sliced)
print("The list of sliced strings are :- ",l1)
