list=[]
ele=input("Enter the string :- ")
string=ele.lower()
vowels=["a","e","i","o","u"]
for i in string:
   if i in vowels:
       list.append(i)
print(f"The vowels in the word  '{ele}' is :- ",list)
