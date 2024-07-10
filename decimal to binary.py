num=int(input("Enter the number"))
l=list()
while num!=0:
    r=num%2
    l.append(r)
    num=num//2
l.reverse
for ele in l:
    print(ele,end="")
