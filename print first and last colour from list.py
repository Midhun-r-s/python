n=int(input("Enter the number of colours :- "))
color=[]
for i in range(n):
    n1=input("Enter the colours :- ")
    color.append(n1)

print("The entered list is :- ",color)
print("The first colour is ",color[0], "and last colour is",color[n-1])

