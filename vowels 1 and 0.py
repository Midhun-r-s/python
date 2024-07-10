list=[]
li1=[]
li2=[]
ele=input("Enter the string :- ")
string=ele.lower()
vowels=["a","e","i","o","u"]
count=0
consonants=0
for i in string:
    li2.append(i)
    if i in vowels:
       list.append(i)
       li1.append(1)
       count=count+1
    else:
       li1.append(0)
       consonants=consonants+1

print(li2)
print(li1)      
print(f"The vowels in the word  '{ele}' is :- ",list)
print(f"The number of vowels in '{ele}' is :- ",count)
print(f"The number of consonants in '{ele}' is :- ",consonants)
