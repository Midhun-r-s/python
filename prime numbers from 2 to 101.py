for i in range(1,101):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=count
    if count==2:
        print(i,end="  ")
