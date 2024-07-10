n=4
for i in range(n):
    for j in range(n):
        if (i==0 or i==3) or (i==1 and j==0) or (i==1 and j==3) or (i==2 and j==0) or (i==2 and j==3):
            print(j+1,end=" ")
        elif (i==1 or i==2) and (j==1 or j==2):
            print(" ",end=" ")
    print()
