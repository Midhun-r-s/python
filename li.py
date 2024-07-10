n=int(input('Enter the Size of Array'))
a=[]
for i in range(n):
    data=int(input('Enter the Data:'))
    a.append(data)
min=a[0]
for i in range(n):
    if a[i]<min:
        min=a[i]
print("The Smallest Element is",min)
