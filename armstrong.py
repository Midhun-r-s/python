r=int(input("Enter the range:- "))
for i in range(0,r+1):
    num=i
    result=0
    n=len(str(i))
    while(i!=0):
        digit=i%10
        result=result+digit**n
        i=i//10
    if num==result:
        print(num)
    
      
            
